from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct

class NetworkACL(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpcweb, vpcadmin, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpcweb_nacl = ec2.NetworkAcl(
            self, "Web NACL",
            vpc=vpcweb,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        vpcweb_nacl.add_entry(
            id="Allow all inbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl.add_entry(
            id="Allow all outbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl.add_entry(
            id="Allow all inbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl.add_entry(
            id="Allow all outbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl_private = ec2.NetworkAcl(
            self, "Web Private NACL",
            vpc=vpcweb,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            )
        )

        vpcweb_nacl_private.add_entry(
            id="Allow SSH inbound from Admin VPC",
            cidr=ec2.AclCidr.ipv4('10.10.10.0/24'),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl_private.add_entry(
            id=f"Allow HTTP inside VPC NACL",
            cidr=ec2.AclCidr.ipv4('10.10.10.0/24'),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl_private.add_entry(
            id=f"Allow ephemeral from Internet NACL",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl_private.add_entry(
            id="Allow HTTP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl_private.add_entry(
            id="Allow HTTPS to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcweb_nacl_private.add_entry(
            id="Allow ephemeral to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

# created NACL for admin server

        vpcadmin_nacl = ec2.NetworkAcl(
            self, "Admin NACL",
            vpc=vpcadmin,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        vpcadmin_nacl.add_entry(
            id="Allow SSH inbound from admin pc",
            cidr=ec2.AclCidr.ipv4('10.20.20.0/24'),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow SSH outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow RDP inbound",
            cidr=ec2.AclCidr.ipv4('10.20.20.0/24'),
            rule_number=220,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow RDP outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=220,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow HTTP inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow HTTP outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow HTTPS inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=240,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        vpcadmin_nacl.add_entry(
            id="Allow HTTPS outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=240,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )
