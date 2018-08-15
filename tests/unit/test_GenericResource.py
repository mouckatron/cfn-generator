
import unittest
import yaml

import cfngenerator

# Type: AWS::EC2::Instance
# Properties:
#   Affinity: String
#   AvailabilityZone: String
#   BlockDeviceMappings:
#     - EC2 Block Device Mapping
#   CreditSpecification: CreditSpecification
#   DisableApiTermination: Boolean
#   EbsOptimized: Boolean
#   ElasticGpuSpecifications: [ ElasticGpuSpecification, ... ]
#   HostId: String
#   IamInstanceProfile: String
#   ImageId: String
#   InstanceInitiatedShutdownBehavior: String
#   InstanceType: String
#   Ipv6AddressCount: Integer
#   Ipv6Addresses:
#     - IPv6 Address Type
#   KernelId: String
#   KeyName: String
#   LaunchTemplate: Amazon EC2  Instance LaunchTemplateSpecification
#   Monitoring: Boolean
#   NetworkInterfaces:
#     - EC2 Network Interface
#   PlacementGroupName: String
#   PrivateIpAddress: String
#   RamdiskId: String
#   SecurityGroupIds:
#     - String
#   SecurityGroups:
#     - String
#   SourceDestCheck: Boolean
#   SsmAssociations:
#     - SSMAssociation
#   SubnetId: String
#   Tags:
#     - Resource Tag
#   Tenancy: String
#   UserData: String
#   Volumes:
#     - EC2 MountPoint
#   AdditionalInfo: String


class TestGenericResource(unittest.TestCase):

    def testCreate(self):
        subject = None
        subject = cfngenerator.GenericResource('TestType')
        assert subject is not None

    def testSetType(self):
        output = "AWS::EC2::Instance"

        subject = cfngenerator.GenericResource(Type=output)

        self.assertEqual(subject['Type'], output)

    def testSetAttribute(self):
        output = "TestValue"

        subject = cfngenerator.GenericResource('TestType')
        subject.TestAttribute = output

        self.assertEqual(subject['Properties']['TestAttribute'], output)
