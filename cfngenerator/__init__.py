import gzip
import json
import yaml

name = 'cfngenerator'


def load(filename='CloudFormationResourceSpecification.json'):
    with gzip.open(filename, 'rb') as f:
        ResourceSpec = json.loads(f.read().decode('utf-8'))

    for name in ResourceSpec['ResourceTypes']:
        class_factory(name, ResourceSpec['ResourceTypes'][name])


def class_factory(name, spec):
    class_type = name
    class_name = name.split('::')[1] + '_' + name.split('::')[2]

    newclass = type(class_name, (GenericResource,), {
        'Type': class_type})

    globals()[class_name] = newclass


class CFTemplate(object):

    def __init__(self, description=''):
        self.resources = []
        self.description = description
        self._type_count = {}

    def add(self, resource):
        type_name = resource.__class__.__name__.split('_')[1]
        resource_name = type_name + self.get_next_type_id(resource)
        dict.__setattr__(resource, 'resource_name', resource_name)
        self.resources.append(resource)

    def get_resources_for_output(self):
        output_resources = {}
        for resource in self.resources:

            for parameter in resource['Properties']:
                if isinstance(resource['Properties'][parameter], GenericResource):
                    resource['Properties'][parameter] = '!Ref {}'.format(resource.resource_name)

            output_resources[resource.resource_name] = dict(resource)

        return output_resources or None

    def get_next_type_id(self, resource):
        type_name = resource.__class__.__name__.split('_')[1]
        try:
            self._type_count[type_name]
        except KeyError:
            self._type_count[type_name] = 0
        else:
            self._type_count[type_name] += 1

        return str(self._type_count[type_name])

    def output(self):
        output_dict = {
            'AWSTemplateFormatVersion': '2010-09-09',
            'Description': self.description,
            'Resources': self.get_resources_for_output()
        }

        return yaml.dump(output_dict,
                         default_flow_style=False)


class GenericResource(dict):
    def __init__(self, **kwargs):
        self['Type'] = self.Type
        self['Properties'] = dict()
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        dict.__init__(self)

    def __setattr__(self, key, value):
        self['Properties'][key] = value
