name = 'cfngenerator'


class CFTemplate(object):

    def __init__(self, description=''):
        self.resources = []
        self.description = description

    def add(self, resource):
        self.resources.append(resource)

    def __str__(self):
        output = """AWSTemplateFormatVersion: 2010-09-09
Description: {description}
""".format(description=self.description)

        for x in self.resources:
            resources_output = "\n".join([x.__str__() for x in self.resources])

        return output + resources_output


class EC2Instance(object):

    def __init__(self, AvailabilityZone='', ImageId='', InstanceType=''):
        self.AvailabilityZone = AvailabilityZone
        self.ImageId = ImageId
        self.InstanceType = InstanceType

    def __str__(self):
        return """Type: AWS::EC2::Instance
Properties:
  AvailabilityZone: {AvailabilityZone}
  ImageId: {ImageId}
  InstanceType: {InstanceType}""".format(**self.__dict__())

    def __dict__(self):
        return {
            'AvailabilityZone': self.AvailabilityZone,
            'ImageId': self.ImageId,
            'InstanceType': self.InstanceType
            }
