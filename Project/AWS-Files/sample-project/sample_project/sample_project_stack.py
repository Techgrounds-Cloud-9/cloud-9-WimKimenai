from constructs import Construct
from .networkacl import NetworkACL
from .bucket import bucket
import boto3

from aws_cdk import (
    Duration,
    RemovalPolicy,
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_assets as Asset,
    aws_s3_deployment as deploys3
)

class SampleProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC 1
        self.vpcweb = ec2.Vpc(
            self, 'WebVPC',
            ip_addresses = ec2.IpAddresses.cidr('10.10.10.0/24'),
            availability_zones= ['eu-central-1a'],
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name = 'WebPublic',
                    subnet_type = ec2.SubnetType.PUBLIC,
                    cidr_mask = 26
                )
            ])

        # VPC 2
        self.vpcadmin = ec2.Vpc(
            self, 'AdminVPC',
            ip_addresses = ec2.IpAddresses.cidr('10.20.20.0/24'),
            availability_zones= ['eu-central-1b'],
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name = 'AdminPublic',
                    subnet_type = ec2.SubnetType.PUBLIC,
                    cidr_mask = 26
                )
            ]
            )

        # VPC Peering Connection
        self.VPCPeeringConnection = ec2.CfnVPCPeeringConnection(
            self, "peer_vpc_id",
            peer_vpc_id = self.vpcadmin.vpc_id,
            vpc_id = self.vpcweb.vpc_id,
        )

        for subnet in self.vpcweb.public_subnets:
            ec2.CfnRoute(
                self, 'VPC Web Peer Route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.20.20.0/24',
                vpc_peering_connection_id=self.VPCPeeringConnection.ref,
            )

        for subnet in self.vpcadmin.public_subnets:
            ec2.CfnRoute(
                self, 'VPC Admin Peer Route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.10.10.0/24',
                vpc_peering_connection_id=self.VPCPeeringConnection.ref,
            )

        #NetworkACL
        networkacl = NetworkACL(
            self, 'Network ACL',
            vpcweb = self.vpcweb,
            vpcadmin = self.vpcadmin,
        )

        # Web server Role & SG

        # Web Security Group
        WebSG = ec2.SecurityGroup(self, 'WebSecurityGroup',
            vpc = self.vpcweb,
            allow_all_outbound = True,
            description = 'Web VPC Security Group'
            )

        # Web Security Group Add Rule
        WebSG.add_ingress_rule(
            peer = ec2.Peer.any_ipv4(),
            connection = ec2.Port.tcp(22),
            description ='SSH'
        )    

        # Web Security Group Add Rule
        WebSG.add_ingress_rule(
            peer = ec2.Peer.any_ipv4(),
            connection = ec2.Port.tcp(80),
            description = 'HTTP'
        )

        # Web Security Group Add Rule
        WebSG.add_ingress_rule(
            peer = ec2.Peer.any_ipv4(),
            connection = ec2.Port.tcp(443),
            description = 'HTTPS'
        )

        # Admin Security Group
        AdminSG = ec2.SecurityGroup(self, 'AdminSecurityGroup',
            vpc = self.vpcadmin,
            allow_all_outbound = True,
            description = 'Admin VPC Security Group'
            )

        # Admin Security Group Add Rule
        AdminSG.add_ingress_rule(
            peer = ec2.Peer.ipv4('213.10.101.81/32'),
            connection = ec2.Port.tcp(22),
            description = 'SSH'
        )    

        # Admin Security Group Add Rule
        AdminSG.add_ingress_rule(
            peer = ec2.Peer.ipv4('213.10.101.81/32'),
            connection = ec2.Port.tcp(3389),
            description = 'RDP'
        )


        # WebS3Read = iam.Role(
        #     self, 'webserver-role',
        #     assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
        #     managed_policies=[
        #         iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
        #         ],
        # )

        #S3 Bucket

        self.userdatas3bucket = s3.Bucket(
            self, "scriptbucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            enforce_ssl=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        self.deployment = deploys3.BucketDeployment(
            self, 'Deploy S3',
            destination_bucket=self.userdatas3bucket,
            sources=[deploys3.Source.asset("./sample_project/scripts/")]
            )
        
        # self.userdatas3bucket.add_to_resource_policy(
        #     iam.PolicyStatement(
        #         effect=iam.Effect.ALLOW,
        #         principals=[iam.ServicePrincipal('ec2.amazonaws.com')],
        #         actions=['s3:GetObject'],
        #         resources=[f'{self.userdatas3bucket.bucket_arn}/*'])
        # )

        userdata_webserver = ec2.UserData.for_linux()
        file_script_path = userdata_webserver.add_s3_download_command(
            bucket=self.userdatas3bucket,
            bucket_key="user_data.sh",
        )

        # userdata_webserver.add_execute_file_command(file_path=file_script_path)

        # userdata_webserver.add_commands("chmod 755 -R /var/www/html/")

        # EC2 Web Server
        EC2instance1 = ec2.Instance(self, 'webserver',
            instance_type = ec2.InstanceType('t2.micro'),
            machine_image = ec2.MachineImage.latest_amazon_linux(
                generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                edition = ec2.AmazonLinuxEdition.STANDARD
            ),
            vpc = self.vpcweb,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=True,)
                )
            ],
            # role = WebS3Read,
            user_data=userdata_webserver,
            security_group=WebSG,
            key_name = 'WKimenaiKP',
        )


        # EC2 Admin / Management Server
        EC2instance2 = ec2.Instance(self, 'adminserver',
            instance_type = ec2.InstanceType('t2.micro'),
            machine_image = ec2.MachineImage.latest_windows(
                version = ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
                ),
            vpc = self.vpcadmin,
             block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=True,)
                )
            ],
            security_group=AdminSG,
            key_name = 'WKimenaiKP',
        )

        # S3 Read Perms

        self.userdatas3bucket.grant_read(EC2instance1)

        userdata_webserver.add_execute_file_command(file_path=file_script_path)

        userdata_webserver.add_commands("chmod 755 -R /var/www/html/")

        # EC2instance1.user_data.add_commands("chmod 755 -R /var/www/html/")

        # EC2instance1 = ec2.UserData.for_linux()

        # userdatabucket = bucket(self, 'UserdataBucket', resource_access=[EC2instance1, EC2instance2])
        
        # userdatapath = EC2instance1.user_data.add_s3_download_command(
        #     bucket=self.userdatas3bucket,
        #     bucket_key='user_data.sh',
        # )

        # EC2instance1.user_data.add_execute_file_command(file_path=userdatapath)
