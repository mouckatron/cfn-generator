
import unittest
import yaml

import cfngenerator


class TestCFTemplate(unittest.TestCase):

    def setUp(self):
        cfngenerator.load(filename='tests/resources/TestSpec.json.gz')

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
            'GeneratedClass0': {
                'Type': 'AWS::SomeService::GeneratedClass',
                'Properties': {
                    'Parameter1': 'az-1',
                    'Parameter2': 'ami-12345678'
                    }
                },
            'GeneratedClass1': {
                'Type': 'AWS::SomeService::GeneratedClass',
                'Properties': {
                    'Parameter1': 'az-2',
                    'Parameter2': 'ami-23456789'
                    }
                }
            }

        subject = cfngenerator.CFTemplate("The Description")
        subject.add(cfngenerator.SomeService_GeneratedClass(Parameter1="az-1", Parameter2="ami-12345678"))
        subject.add(cfngenerator.SomeService_GeneratedClass(Parameter2="ami-23456789", Parameter1="az-2"))

        self.assertEqual(subject.get_resources_for_output(), output)

    def testOutputWithChildren(self):
        output = yaml.dump({'AWSTemplateFormatVersion': '2010-09-09',
                            'Description': 'The Description',
                            'Resources': {
                                'GeneratedClass0': {
                                    'Type': 'AWS::SomeService::GeneratedClass',
                                    'Properties': {
                                        'Parameter1': 'az-1',
                                        'Parameter2': 'ami-12345678'
                                        }
                                    },
                                'GeneratedClass1': {
                                    'Type': 'AWS::SomeService::GeneratedClass',
                                    'Properties': {
                                        'Parameter1': 'az-2',
                                        'Parameter2': 'ami-23456789'
                                    }
                                }
                            }},
                           default_flow_style=False)

        subject = cfngenerator.CFTemplate("The Description")
        subject.add(cfngenerator.SomeService_GeneratedClass(Parameter1="az-1", Parameter2="ami-12345678"))
        subject.add(cfngenerator.SomeService_GeneratedClass(Parameter1="az-2", Parameter2="ami-23456789"))

        self.assertEqual(subject.output(), output)

    def testOutputWithReferences(self):
        return
        output = yaml.dump({'AWSTemplateFormatVersion': '2010-09-09',
                            'Description': 'The Description',
                            'Resources': {
                                'GeneratedClass0': {
                                    'Type': 'AWS::SomeService::GeneratedClass',
                                    'Properties': {
                                        'Parameter1': 'az-1',
                                        'Parameter2': 'ami-12345678'
                                        }
                                    },
                                'GeneratedClass1': {
                                    'Type': 'AWS::SomeService::GeneratedClass',
                                    'Properties': {
                                        'Parameter1': 'az-2',
                                        'Parameter2': '!Ref GeneratedClass0'
                                    }
                                }
                            }},
                           default_flow_style=False)

        subject = cfngenerator.CFTemplate("The Description")
        subject_child1 = cfngenerator.SomeService_GeneratedClass(Parameter1="az-1",
                                                                 Parameter2="ami-12345678")
        subject.add(subject_child1)
        subject.add(cfngenerator.SomeService_GeneratedClass(Parameter1="az-2",
                                                            Parameter2=subject_child1))

        self.assertEqual(subject.output(), output)
