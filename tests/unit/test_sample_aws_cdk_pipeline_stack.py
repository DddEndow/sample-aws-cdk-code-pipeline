import json
import pytest

from aws_cdk import core
from sample-aws-cdk-pipeline.sample_aws_cdk_pipeline_stack import SampleAwsCdkPipelineStack


def get_template():
    app = core.App()
    SampleAwsCdkPipelineStack(app, "sample-aws-cdk-pipeline")
    return json.dumps(app.synth().get_stack("sample-aws-cdk-pipeline").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
