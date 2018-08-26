
import unittest
import yaml

import cfngenerator


class TestGenericResource(unittest.TestCase):

    def testCreate(self):
        cfngenerator.GenericResource.Type = 'SomeType'

        subject = None
        subject = cfngenerator.GenericResource()

        assert subject is not None

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
