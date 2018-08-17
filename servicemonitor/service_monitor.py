import logging

from servicemonitor.config_logging import setup_logging
from servicemonitor.http_utils import trigger_get_request
from servicemonitor.yaml_utils import parse_yaml_to_objects

setup_logging()

service_list_path = '../resources/service_list.yml'
target_object = "Service"

services = parse_yaml_to_objects(service_list_path, target_object)

for service in services:
    for uri in service.uris:
        logging.info(trigger_get_request(service.hostname, service.port, uri))
