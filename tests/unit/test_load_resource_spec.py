
import unittest
import unittest.mock

import cfngenerator


class TestLoadResourceSpec(unittest.TestCase):

    def testExists(self):

        self.assertIsInstance(cfngenerator.load, object)

    def testCallsClassFactory(self):

        cfngenerator.class_factory = unittest.mock.Mock()

        cfngenerator.load('tests/resources/TestSpec.json.gz')

        cfngenerator.class_factory.assert_called()
