from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_s3 as s3
)

class SampleProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC 1
        self.vpcweb = ec2.Vpc(
            self, 'WebVPC',
            ip_addresses = ec2.IpAddresses.cidr('10.10.10.0/24'),
            availability_zones= ['eu-central-1a', 'eu-central-1b'],
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
            availability_zones= ['eu-central-1a', 'eu-central-1b'],
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name = 'AdminPublic',
                    subnet_type = ec2.SubnetType.PUBLIC,
                    cidr_mask = 26
                )
            # route_table_id = 
            ])
        
        # EC2 Web Server
        EC2instance1 = ec2.Instance(self, 'webserver',
            instance_type = ec2.InstanceType('t2.micro'),
            machine_image = ec2.MachineImage.latest_amazon_linux(
                generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                edition = ec2.AmazonLinuxEdition.STANDARD
            ),
            vpc = self.vpcweb)

        # EC2 Admin / Management Server
        EC2instance2 = ec2.Instance(self, 'adminserver',
            instance_type = ec2.InstanceType('t2.micro'),
            machine_image = ec2.MachineImage.latest_windows(
                version = ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
                ),
            vpc = self.vpcadmin,
        )

        # VPC Peering Connection
        self.VPCPeeringConnection = ec2.CfnVPCPeeringConnection(
            self, "peer_vpc_id",
            peer_vpc_id = self.vpcweb.vpc_id,
            vpc_id = self.vpcadmin.vpc_id,
        )

        #NetworkACL
        vpc_web_nacl = ec2.NetworkAcl(
            self, 'VPC-1 Web',
            vpc = self.vpcweb,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
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

        # Web Security Group
        WebSG = ec2.SecurityGroup(self, 'WebSecurityGroup',
            vpc = self.vpcweb,
            allow_all_outbound = True,
            description = 'Web VPC Security Group'
            )

        # Web Security Group Add Rule
        WebSG.add_ingress_rule(
            peer = ec2.Peer.ipv4('213.10.101.81/32'),
            connection = ec2.Port.tcp(22),
            description ='SSH'
        )    

        # Web Security Group Add Rule
        WebSG.add_ingress_rule(
            peer = ec2.Peer.ipv4('213.10.101.81/32'),
            connection = ec2.Port.tcp(80),
            description = 'HTTP'
        )

        # Web Security Group Add Rule
        WebSG.add_ingress_rule(
            peer = ec2.Peer.ipv4('213.10.101.81/32'),
            connection = ec2.Port.tcp(443),
            description = 'HTTPS'
        )

        # S3 Bucket
        self.s3bucket = s3.Bucket(
        self, 'wimtechgrounds-userdata',
        encryption=s3.BucketEncryption.S3_MANAGED,
        versioned=True,
        enforce_ssl=True,
        removal_policy = RemovalPolicy.DESTROY,
        )
