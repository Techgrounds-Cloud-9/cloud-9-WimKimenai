from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct

class NetworkACL(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpcweb, vpcadmin, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpcweb_nacl = ec2.NetworkAcl(
            self, 'VPC Web ACL',
            vpc = vpcweb,
            subnet_selection = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            )
        )

        # Add rules to Network ACL
        vpcweb_nacl.add_entry(
            'HTTP inbound allow',
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcweb_nacl.add_entry(
            'HTTP outbound allow',
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcweb_nacl.add_entry(
            'HTTPS inbound allow',
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcweb_nacl.add_entry(
            'HTTPS outbound allow',
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcweb_nacl.add_entry(
            'SSH inbound allow',
            cidr = ec2.AclCidr.ipv4('10.20.20.0/24'),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcweb_nacl.add_entry(
            'Ephemeral outbound allow',
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcweb_nacl.add_entry(
            'Ephemeral inbound allow',
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW
        )

        #Network ACL for Admin Server
        vpcadmin_nacl = ec2.NetworkAcl(
            self, 'VPC Admin ACL',
            vpc = vpcadmin,
            subnet_selection = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            )
        )

        # Add rules to Network ACL
        vpcadmin_nacl.add_entry(
            'SSH inbound allow Subnet',
            cidr = ec2.AclCidr.ipv4('10.10.10.0/24'),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcadmin_nacl.add_entry(
            'SSH outbound allow Subnet',
            cidr = ec2.AclCidr.ipv4('10.10.10.0/24'),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW
        )

        
        # Add all trusted IP addresses 
        vpcadmin_nacl.add_entry(
            'SSH inbound allow AdminIP',
            cidr = ec2.AclCidr.ipv4('213.10.101.81/32'),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW

        )

        vpcadmin_nacl.add_entry(
            'Outbound allow AdminIP',
            cidr = ec2.AclCidr.ipv4('213.10.101.81/32'),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW
        )

        vpcadmin_nacl.add_entry(
            'Inbound allow RDP',
            cidr = ec2.AclCidr.ipv4('213.10.101.81/32'),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port(3389),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW
        )

        # create and configure NACL for webserver private
        webvpc_priv_nacl = ec2.NetworkAcl(
            self, "VPC Web Private Subnet NACL",
            vpc=vpcweb,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            )
        )      

        # add inbound and outbound rules for the webserver NACL

        webvpc_priv_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_priv_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_priv_nacl.add_entry(
            id="Allow SSH inbound from anywhere",
            cidr=ec2.AclCidr.ipv4('10.10.10.0/24'),
            rule_number=130,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_priv_nacl.add_entry(
            id="Allow SSH outbound from anywhere",
            cidr=ec2.AclCidr.ipv4('10.10.10.0/24'),
            rule_number=130,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_priv_nacl.add_entry(
            id="Private Web Allow HTTP inbound from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_priv_nacl.add_entry(
            id="Private Web Allow HTTP outbound from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )