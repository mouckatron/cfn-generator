name = 'cfngenerator'


class CFTemplate(object):

    def __init__(self, description=''):
        self.description = description

    def __str__(self):
        return 'AWSTemplateFormatVersion: "2010-09-09"\
Description: "{description}"'.format(description=self.description)


class EC2Instance(object):

    def __init__(self, AvailabilityZone='', ImageId='', InstanceType=''):
        pass

    def
