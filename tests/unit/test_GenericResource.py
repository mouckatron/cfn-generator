
import unittest
import json

import cfngenerator


class TestGenericResource(unittest.TestCase):

    def testCreate(self):
        cfngenerator.GenericResource.Type = 'SomeType'

        subject = None
        subject = cfngenerator.GenericResource()

        self.assertIsNotNone(subject)

    def testSetType(self):
        output = "SomeType"
        cfngenerator.GenericResource.Type = output

        subject = cfngenerator.GenericResource()

        self.assertEqual(subject['Type'], output)

    def testSetAttribute(self):
        output = "SomeValue"
        cfngenerator.GenericResource.Type = 'SomeType'

        subject = cfngenerator.GenericResource()
        subject.TestAttribute = output

        self.assertEqual(subject['Properties']['TestAttribute'], output)


class TestGenericResourceWithSpec(unittest.TestCase):

    def setUp(self):
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

    def testGeneratedClassWithCorrectParameters(self):
        return

        cfngenerator.SomeService_GeneratedClass(Parameter1='a value',
                                                Parameter2='another value')

    def testGeneratedClassWithIncorrectParameter(self):
        return

    def testGeneratedClassWithMissingParameter(self):
        return
