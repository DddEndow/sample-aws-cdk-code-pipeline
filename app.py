#!/usr/bin/env python3

from aws_cdk import core

from sample_aws_cdk_pipeline.sample_aws_cdk_pipeline_stack import SampleAwsCdkPipelineStack
from continuous_delivery.continuous_delivery_stack import ContinuousDeliveryStack

app = core.App()
sample_aws_cdk_pipeline_stack = SampleAwsCdkPipelineStack(app, "sample-aws-cdk-pipeline", env={'region': 'eu-west-2'})

ContinuousDeliveryStack(app, id="continuous-delivery", deploy_stack=sample_aws_cdk_pipeline_stack, env={'region': 'eu-west-2'})

app.synth()
