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
    aws_s3_deployment as deploys3,
    aws_backup as backup,
    aws_events as events,
    aws_kms as kms,
    aws_elasticloadbalancingv2 as elb,
    aws_autoscaling as autoscaling,
    aws_certificatemanager as acm,
)

class SampleProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC 1
        self.vpcweb = ec2.Vpc(
            self, 'WebVPC',
            ip_addresses = ec2.IpAddresses.cidr('10.10.10.0/24'),
            max_azs=3,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name = 'WebPublic',
                    subnet_type = ec2.SubnetType.PUBLIC,
                    cidr_mask = 26
                ),
                ec2.SubnetConfiguration(
                    name="Private_Web_VPC", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
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

        name_count = 0


        for subnet in self.vpcweb.public_subnets:
            name_count += 1
            ec2.CfnRoute(self, "admin_to_web_route" + str(name_count),
            route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.20.20.0/24',
                vpc_peering_connection_id=self.VPCPeeringConnection.ref,
            )


        for subnet in self.vpcadmin.public_subnets:
            name_count += 1
            ec2.CfnRoute(self, "VPC Admin Peer Route" + str(name_count),
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

        # KMS Module

        AdminKMS_key = kms.Key(self, "AdminKey",
            enable_key_rotation = True,
            alias = "AdminKMS_key",
            pending_window=Duration.days(10),
            removal_policy = RemovalPolicy.DESTROY)
        self.adminkms_key = AdminKMS_key

        WebKMS_key = kms.Key(self, "WebKey",
            enable_key_rotation = True,
            alias = "WebKMS_key",
            pending_window=Duration.days(10),
            removal_policy = RemovalPolicy.DESTROY)
        self.webkms_key = WebKMS_key

        # VaultKMS_key = kms.Key(self, "VaultKey",
        #     enable_key_rotation = True,
        #     alias = "VaultKMS_key",
        #     pending_window=Duration.days(10),
        #     removal_policy = RemovalPolicy.DESTROY)
        # self.vaultkms_key = VaultKMS_key


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
            sources=[deploys3.Source.asset("./sample_project/scripts")]
            )


        # Auto Scaling

        self.user_data = ec2.UserData.for_linux()


        launchtemplaterole = iam.Role(
            self,
            "Launch Template Role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        # Launch Template
        self.launch_temp = ec2.LaunchTemplate(
            self, "Launch template",
            launch_template_name="web_server_template",
            instance_type=ec2.InstanceType("t2.micro"),
            key_name="WKimenaiKP",
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            role=launchtemplaterole,
            user_data=self.user_data,
            security_group=WebSG,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=True,    
                    )
                )
            ]    
        )

        # Auto scaling group
        self.as_group = autoscaling.AutoScalingGroup(
            self, "Auto Scaling_Group",
            vpc=self.vpcweb,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            launch_template=self.launch_temp,
            min_capacity=1,
            max_capacity=3,
        )

        # AUTO SCALING scaling policy
        self.as_group.scale_on_cpu_utilization(
            "cpu auto scaling",
            target_utilization_percent=80,
        )

        # LOAD BALANCER
        self.elb = elb.ApplicationLoadBalancer(
            self, "Application Load Balancer",
            vpc=self.vpcweb,
            security_group=WebSG,
            internet_facing=True,
        )
        # self.elb.add_redirect()

        http_listener = self.elb.add_listener(
            "HTTP listener",
            port=80,
            open=True,
        )

        web_target_group = http_listener.add_targets(
            "ASG webserver",
            port=80,
            targets=[self.as_group],
            health_check=elb.HealthCheck(
                enabled=True,
            ),
        )

        # SSL Certificate ARN
        # arn = "arn:aws:acm:eu-central-1:663303000432:certificate/7a324a63-01ba-438c-b7a6-95b6b4e4aecb"

        # call the certificate itself
        # certificate = acm.Certificate.from_certificate_arn(self, "SSL Cert", arn)

        # https_listener = self.elb.add_listener(
        #     "Listener for HTTPS",
        #     port=443,
        #     open=True,
        #     ssl_policy=elb.SslPolicy.FORWARD_SECRECY_TLS12,
        #     certificates=[certificate],
        # )

        # asg_target_group = https_listener.add_targets(
        #     "ASG webserver",
        #     port=80,
        #     targets=[self.as_group],
        #     health_check=elb.HealthCheck(
        #         enabled=True,
        #         port="80",
        #     ),
        #     stickiness_cookie_duration=Duration.minutes(5),
        #     stickiness_cookie_name="pbc",
        # )

        asg_userdata = self.as_group.user_data.add_s3_download_command(
            bucket=self.userdatas3bucket,
            bucket_key="user_data.sh"
        )

        # execute the userdata file
        self.as_group.user_data.add_execute_file_command(file_path=asg_userdata)


        # Elastic Load Balancer
        # self.elb = elb.ApplicationLoadBalancer(
        #     self, "Application Load Balancer",
        #     vpc=self.vpcweb,
        #     internet_facing=True,
        # )
        # self.elb.add_redirect()
        

        # EC2 Web Server
        # EC2instance1 = ec2.Instance(self, 'webserver',
        #     instance_type = ec2.InstanceType('t2.micro'),
        #     machine_image = ec2.MachineImage.latest_amazon_linux(
        #         generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
        #         edition = ec2.AmazonLinuxEdition.STANDARD
        #     ),
        #     vpc = self.vpcweb,
        #     block_devices=[
        #         ec2.BlockDevice(
        #             device_name="/dev/xvda",
        #             volume=ec2.BlockDeviceVolume.ebs(
        #                 volume_size=8,
        #                 encrypted=True,
        #                 kms_key = WebKMS_key,
        #                 delete_on_termination=True,)
        #         )
        #     ],
        #     security_group=WebSG,
        #     key_name = 'WKimenaiKP',
        # )


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
                        kms_key = AdminKMS_key,
                        delete_on_termination=True,)
                )
            ],
            security_group=AdminSG,
            key_name = 'WKimenaiKP',
        )

        # S3 Read Perms

        self.userdatas3bucket.grant_read(launchtemplaterole)

        file_script_path = self.launch_temp.user_data.add_s3_download_command(
            bucket=self.userdatas3bucket,
            bucket_key="user_data.sh",
        )

        self.launch_temp.user_data.add_execute_file_command(file_path=file_script_path)

        # # Backup
        # self.backup_vault = backup.BackupVault(
        #     self, 'BackupVault',
        #     backup_vault_name='BackupVault',
        #     )

        # # Backup Plan
        # self.backup_plan = backup.BackupPlan(
        #     self, 'BackupPlan',
        #     backup_vault=self.backup_vault
        #     )

        # self.backup_vault.apply_removal_policy(RemovalPolicy.DESTROY)
        # self.backup_plan.apply_removal_policy(RemovalPolicy.DESTROY)

        # # Backup Resources
        # self.backup_plan.add_selection('Backup Selection',
        #     resources=[
        #         backup.BackupResource.from_ec2_instance(EC2instance2),
        #         ],
        #     allow_restores=True,
        #     )
        
        # # Add backup rules
        # self.backup_plan.add_rule(backup.BackupPlanRule(
        #     enable_continuous_backup=True,
        #     delete_after=Duration.days(7),
        #     schedule_expression=events.Schedule.cron(
        #         hour="4",
        #         minute="0",
        #         ))
        #     )
