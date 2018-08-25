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

    def add(self, resource):
        self.resources.append(resource)

    def get_resources_for_output(self):
        type_count = {}
        output_resources = {}
        for x in self.resources:
            type_name = x.__class__.__name__.split('_')[1]
            try:
                type_count[type_name]
            except KeyError:
                type_count[type_name] = 0
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
    def __init__(self, **kwargs):
        self['Type'] = self.Type
        self['Properties'] = dict()
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        dict.__init__(self)

    def __setattr__(self, key, value):
        self['Properties'][key] = value
