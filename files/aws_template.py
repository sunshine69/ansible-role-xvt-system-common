#!/usr/bin/env python
import argparse
import json

import boto.cloudformation
import boto.ec2
import boto.utils

from jinja2 import Template, Environment, FileSystemLoader

def json_pretty(value):
    print json.dumps(value, sort_keys=True, indent=2, separators=(',', ': '))

def instance_metadata():
    meta = boto.utils.get_instance_metadata()
    region = meta['placement']['availability-zone'][:-1]

    ec2_conn = boto.ec2.connect_to_region(region)
    instance = ec2_conn.get_only_instances(instance_ids=[meta['instance-id']])[0]

    meta['region'] = region
    meta['tags'] = instance.tags
    meta['cloudformation_stack'] = instance.tags['aws:cloudformation:stack-name']
    return meta

META = instance_metadata()
AWS_CONNECTION = boto.cloudformation.connect_to_region(META['region'])

CONTEXT = {
    'metadata': META
}

def cfn_resource(name):
    response = AWS_CONNECTION.describe_stack_resource(META['cloudformation_stack'], name)
    return response['DescribeStackResourceResponse']['DescribeStackResourceResult']['StackResourceDetail']

class TemplateRender:

    def __init__(self, template):
        self.env = Environment(loader=FileSystemLoader('.'))
        self.env.globals.update(cfn_resource=cfn_resource)
        self.template = self.env.get_template(template)

    def render(self):
        print self.template.render(CONTEXT)

class App:

    description = 'Tool to generate file from template based on the AWS settings'

    def __init__(self):
        self.setup_argparse()

    def setup_argparse(self):
        self.cmd_parser = argparse.ArgumentParser(description=self.description)
        self.cmd_parser.add_argument('--template', help='template file')
        self.cmd_parser.add_argument('--cfn-resource', dest='cfn_resource', help='Display CloudFormation resource')
        self.cmd_parser.add_argument('--context', action='store_true', dest='context', help='Display context information')

    def run(self):
        args = self.cmd_parser.parse_args()
        if args.template:
            TemplateRender(args.template).render()
        elif args.cfn_resource:
            json_pretty(cfn_resource(args.cfn_resource))
        elif args.context:
            json_pretty(CONTEXT)


if __name__ == '__main__':
    app = App()
    app.run()
