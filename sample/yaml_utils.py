from collections import namedtuple

import yaml


def parse_yaml_to_objects(path, target_class):
    raw_data = yaml.safe_load(open(path))
    service_list = raw_data.get(target_class)
    services = []

    for service in service_list:
        services.append(namedtuple(target_class, service.keys())(*service.values()))

    return services
