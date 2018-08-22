
import unittest
import unittest.mock
import yaml

import cfngenerator


class TestClassFactory(unittest.TestCase):

    def testExists(self):

        self.assertIsInstance(cfngenerator.class_factory, object)

    def testCreateClass(self):

        name = 'GeneratedClass'
        spec = ''  # does not need to be anything. See later tests.

        cfngenerator.class_factory(name, spec)

        self.assertIsInstance(cfngenerator.GeneratedClass, object)

    def testCreateClassWithSpec(self):

        name = 'GeneratedClass'
        spec = '''{AWS::SomeService::GeneratedClass: {
                       Documentation: "http://somewebpage",
                       Properties: {
                           Parameter1: {
                               Documentation: "http://somewebpage/parameter1",
                               PrimitiveType: "String",
                               Required: true,
                               UpdateType: "Immutable"
                           },
                           Parameter1: {
                               Documentation: "http://somewebpage/parameter2",
                               PrimitiveType: "String",
                               Required: false,
                               UpdateType: "Mutable"
                           }
                      }
                  }'''

        cfngenerator.class_factory(name, spec)

        cfngenerator.GeneratedClass(Parameter1='a value',
                                    Parameter2='another value')

    def testGeneratedClassOutput(self):

        name = 'GeneratedClass'
        spec = '''{AWS::SomeService::GeneratedClass: {
                       Documentation: "http://somewebpage",
                       Properties: {
                           Parameter1: {
                               Documentation: "http://somewebpage/parameter1",
                               PrimitiveType: "String",
                               Required: true,
                               UpdateType: "Immutable"
                           },
                           Parameter1: {
                               Documentation: "http://somewebpage/parameter2",
                               PrimitiveType: "String",
                               Required: false,
                               UpdateType: "Mutable"
                           }
                      }
                  }'''
        output = yaml.dump({'Type': 'AWS::SomeService::GeneratedClass', 'Properties': {
            'Parameter1': 'a value',
            'Parameter2': 'another value'}
            }, default_flow_style=False)

        cfngenerator.class_factory(name, spec)

        subject = cfngenerator.GeneratedClass(Parameter1='a value',
                                              Parameter2='another value')

        print(output)
        print(yaml.dump(dict(subject), default_flow_style=False))

        self.assertEqual(yaml.dump(dict(subject), default_flow_style=False), output)
