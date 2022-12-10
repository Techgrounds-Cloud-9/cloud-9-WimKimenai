import aws_cdk as core
import aws_cdk.assertions as assertions

from testproject2.testproject2_stack import Testproject2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in testproject2/testproject2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Testproject2Stack(app, "testproject2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
