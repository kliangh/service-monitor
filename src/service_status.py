from src.http_utils import trigger_get_request

host = "localhost"
port = 8080


def get_health():
    print(trigger_get_request(host, port, "/health"))


def get_metrics():
    print(trigger_get_request(host, port, "/metrics"))


def get_trace():
    print(trigger_get_request(host, port, "/trace"))