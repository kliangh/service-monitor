class Service(object):
    def __init__(self, service_name, hostname, port, uris):
        self.service_name = service_name
        self.hostname = hostname
        self.port = port
        self.uris = uris
