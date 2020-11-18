#!/usr/bin/env python3

from aws_cdk import core

from sample_aws_cdk_pipeline.sample_aws_cdk_pipeline_stack import SampleAwsCdkPipelineStack


app = core.App()
SampleAwsCdkPipelineStack(app, "sample-aws-cdk-pipeline", env={'region': 'us-west-2'})

app.synth()
