
import unittest

import cfngenerator


class TestCFTemplate(unittest.TestCase):

    def testCreate(self):
        subject = None
        subject = cfngenerator.CFTemplate()
        assert subject is not None

    def testBaseOutput(self):
        output = 'AWSTemplateFormatVersion: "2010-09-09"\
Description: "The Description"'

        subject = cfngenerator.CFTemplate("The Description")
        assert subject.__str__() == output

    def testDescription(self):
        output = 'AWSTemplateFormatVersion: "2010-09-09"\
Description: "A Different Description"'

        subject = cfngenerator.CFTemplate("A Different Description")
        assert subject.__str__() == output
