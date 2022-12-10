from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk.aws_ec2 as ec2

class Testproject2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpcweb = ec2.Vpc(
            self, 'WebVPC',
            cidr = '10.10.10.0/24',
            max_azs = 1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name = 'WebPublic',
                    subnet_type = ec2.SubnetType.PUBLIC,
                    cidr_mask = 26
                )
            ])




        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Testproject2Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
