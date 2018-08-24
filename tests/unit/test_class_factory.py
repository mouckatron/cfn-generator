
import unittest
import unittest.mock
import json
import yaml

import cfngenerator


class TestClassFactory(unittest.TestCase):

    def testExists(self):

        self.assertIsInstance(cfngenerator.class_factory, object)

    def testCreateClass(self):

        name = 'AWS::SomeService::GeneratedClass'
        spec = json.loads('{}')  # does not need to be anything. See later tests.

        cfngenerator.class_factory(name, spec)

        self.assertIsInstance(cfngenerator.GeneratedClass, object)

    def testCreateClassWithSpec(self):

        name = 'AWS::SomeService::GeneratedClass'
        spec = json.loads('''{
                       "Documentation": "http://somewebpage",
                       "Properties": {
                           "Parameter1": {
                               "Documentation": "http://somewebpage/parameter1",
                               "PrimitiveType": "String",
                               "Required": true,
                               "UpdateType": "Immutable"
                           },
                           "Parameter2": {
                               "Documentation": "http://somewebpage/parameter2",
                               "PrimitiveType": "String",
                               "Required": false,
                               "UpdateType": "Mutable"
                           }
                      }
                  }''')

        cfngenerator.class_factory(name, spec)

        cfngenerator.GeneratedClass(Parameter1='a value',
                                    Parameter2='another value')

    def testGeneratedClassOutput(self):

        name = 'AWS::SomeService::GeneratedClass'
        spec = json.loads('''{
                       "Documentation": "http://somewebpage",
                       "Properties": {
                           "Parameter1": {
                               "Documentation": "http://somewebpage/parameter1",
                               "PrimitiveType": "String",
                               "Required": true,
                               "UpdateType": "Immutable"
                           },
                           "Parameter2": {
                               "Documentation": "http://somewebpage/parameter2",
                               "PrimitiveType": "String",
                               "Required": false,
                               "UpdateType": "Mutable"
                           }
                      }
                  }''')

        output = yaml.dump({'Type': 'AWS::SomeService::GeneratedClass', 'Properties': {
            'Parameter1': 'a value',
            'Parameter2': 'another value'}
            }, default_flow_style=False)

        cfngenerator.class_factory(name, spec)

        subject = cfngenerator.GeneratedClass(Parameter1='a value',
                                              Parameter2='another value')

        self.assertEqual(yaml.dump(dict(subject), default_flow_style=False), output)
