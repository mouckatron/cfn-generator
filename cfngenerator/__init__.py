import yaml

name = 'cfngenerator'


class CFTemplate(object):

    def __init__(self, description=''):
        self.resources = []
        self.description = description

    def add(self, resource):
        self.resources.append(resource)

    def get_resources_for_output(self):
        type_count = {}
        output_resources = {}
        for x in self.resources:
            type_name = x.__class__.type_name
            try:
                type_count[type_name]
            except KeyError:
                type_count[type_name] = 1
            else:
                type_count[type_name] += 1

            resource_name = type_name + str(type_count[type_name])
            output_resources[resource_name] = dict(x)

        return output_resources or None

    def output(self):
        output_dict = {
            'AWSTemplateFormatVersion': '2010-09-09',
            'Description': self.description,
            'Resources': self.get_resources_for_output()
        }

        return yaml.dump(output_dict,
                         default_flow_style=False)


class GenericResource(dict):

    type_name = 'GenericResource'

    def __init__(self, Type):
        self['Type'] = Type
        self['Properties'] = dict()

    def __setattr__(self, key, value):
        self['Properties'][key] = value


class EC2Instance(GenericResource):

    type_name = 'EC2Instance'

    def __init__(self, AvailabilityZone='', ImageId='', InstanceType=''):
        GenericResource.__init__(self, 'AWS::EC2::Instance')
        self.AvailabilityZone = AvailabilityZone
        self.ImageId = ImageId
        self.InstanceType = InstanceType
        dict.__init__(self)
