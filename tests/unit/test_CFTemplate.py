
import unittest
import yaml

import cfngenerator


class TestCFTemplate(unittest.TestCase):

    def testCreate(self):
        subject = None
        subject = cfngenerator.CFTemplate()
        assert subject is not None

    def testBaseOutput(self):
        output = yaml.dump({'AWSTemplateFormatVersion': '2010-09-09',
                            'Description': 'The Description',
                            'Resources': None},
                           default_flow_style=False)

        subject = cfngenerator.CFTemplate("The Description")
        self.assertEqual(subject.output(), output)

    def testDescription(self):
        output = yaml.dump({'AWSTemplateFormatVersion': '2010-09-09',
                            'Description': 'A Different Description',
                            'Resources': None},
                           default_flow_style=False)

        subject = cfngenerator.CFTemplate("A Different Description")
        self.assertEqual(subject.output(), output)

    def testGetResourcesForOutput(self):
        output = {
            'EC2Instance1': {
                'Type': 'AWS::EC2::Instance',
                'Properties': {
                    'AvailabilityZone': 'az-1',
                    'ImageId': 'ami-12345678',
                    'InstanceType': 'a1.size'
                    }
                },
                'EC2Instance2': {
                'Type': 'AWS::EC2::Instance',
                'Properties': {
                    'AvailabilityZone': 'az-2',
                    'ImageId': 'ami-23456789',
                    'InstanceType': 'b1.size'
                    }
                }
            }

        subject = cfngenerator.CFTemplate("The Description")
        subject.add(cfngenerator.EC2Instance("az-1", "ami-12345678", "a1.size"))
        subject.add(cfngenerator.EC2Instance("az-2", "ami-23456789", "b1.size"))

        self.assertEqual(subject.get_resources_for_output(), output)

    def testOutputWithChildren(self):
        output = yaml.dump({'AWSTemplateFormatVersion': '2010-09-09',
                            'Description': 'The Description',
                            'Resources': {
                                'EC2Instance1': {
                                    'Type': 'AWS::EC2::Instance',
                                    'Properties': {
                                        'AvailabilityZone': 'az-1',
                                        'ImageId': 'ami-12345678',
                                        'InstanceType': 'a1.size'
                                        }
                                    }
                                }
                            },
                           default_flow_style=False)

        subject = cfngenerator.CFTemplate("The Description")
        subject.add(cfngenerator.EC2Instance("az-1", "ami-12345678", "a1.size"))

        self.assertEqual(subject.output(), output)
