from aws_cdk import (
    RemovalPolicy,
    Duration,
    aws_s3 as s3,
    aws_s3_deployment as deploys3,
    aws_iam as iam,
)
from constructs import Construct

class bucket(Construct):

    def __init__(self, scope: Construct, construct_id: str, resource_access, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.userdatas3 = s3.Bucket(
            self, construct_id,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            enforce_ssl=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        self.deployment = deploys3.BucketDeployment(
            self, 'Deploy S3',
            destination_bucket=self.userdatas3,
            sources=[deploys3.Source.asset(r"./sample_project/UserData.zip")]
            )
        
        self.userdatas3.add_to_resource_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[iam.ServicePrincipal('ec2.amazonaws.com')],
                actions=['s3:GetObject'],
                resources=[f'{self.userdatas3.bucket_arn}/*'])
        )