
import unittest
from collections import OrderedDict
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


class TestEC2Instance(unittest.TestCase):

    def testCreate(self):
        subject = None
        subject = cfngenerator.EC2Instance()
        assert subject is not None

    def testBaseOutput(self):
        output = yaml.dump({'Type': 'AWS::EC2::Instance',
                            'Properties': {
                                'AvailabilityZone': 'az-1',
                                'ImageId': 'ami-12345678',
                                'InstanceType': 'a1.size'}
                            }, default_flow_style=False)

        subject = cfngenerator.EC2Instance(AvailabilityZone='az-1',
                                           ImageId='ami-12345678',
                                           InstanceType='a1.size')

        self.assertEqual(yaml.dump(dict(subject), default_flow_style=False), output)

    def testCreateWithDifferentProperties(self):
        output = yaml.dump({'Type': 'AWS::EC2::Instance', 'Properties': {
            'AvailabilityZone': 'az-2',
            'ImageId': 'ami-23456789',
            'InstanceType': 'b1.size'}
            }, default_flow_style=False)

        subject = cfngenerator.EC2Instance(AvailabilityZone='az-2',
                                           ImageId='ami-23456789',
                                           InstanceType='b1.size')

        self.assertEqual(yaml.dump(dict(subject), default_flow_style=False), output)
