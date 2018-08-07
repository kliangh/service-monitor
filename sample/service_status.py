from collections import namedtuple

import yaml

from src.http_utils import trigger_get_request

host = "localhost"
port = 8080

service_list_path = '../resources/service_list.yml'


def get_health():
    print(trigger_get_request(host, port, "/health"))


def get_metrics():
    print(trigger_get_request(host, port, "/metrics"))


def get_trace():
    print(trigger_get_request(host, port, "/trace"))


raw_data = yaml.safe_load(open(service_list_path))

service_list = raw_data.get("service")[0]

services = []

for service in service_list:
    services.append(namedtuple("Service", service_list.keys())(*service_list.values()))

print(type(services))

print(type(services[1]))
