
import unittest

import cfngenerator


class TestCFTemplate(unittest.TestCase):

    def testCreate(self):
        subject = None
        subject = cfngenerator.CFTemplate()
        assert subject is not None

    def testBaseOutput(self):
        output = """AWSTemplateFormatVersion: 2010-09-09
Description: The Description"""

        subject = cfngenerator.CFTemplate("The Description")
        self.assertEqual(subject.__str__(), output)

    def testDescription(self):
        output = """AWSTemplateFormatVersion: 2010-09-09
Description: A Different Description"""

        subject = cfngenerator.CFTemplate("A Different Description")
        self.assertEqual(subject.__str__(), output)

    def testOutputWithChildren(self):
        output = """AWSTemplateFormatVersion: 2010-09-09
Description: The Description
Resources:
  EC2Instance1:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: az1
      ImageId: ami-12345678
      InstanceType: a1.size"""

        subject = cfngenerator.CFTemplate("The Description")
        subject.add(cfngenerator.EC2Instance("az-1", "ami-12345678", "a1.size"))

        self.assertEqual(subject.__str__(), output)
