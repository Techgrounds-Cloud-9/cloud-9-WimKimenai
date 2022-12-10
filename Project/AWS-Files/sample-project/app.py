#!/usr/bin/env python3

import aws_cdk as cdk

from sample_project.sample_project_stack import SampleProjectStack


app = cdk.App()
SampleProjectStack(app, "sample-project")

app.synth()
