import http.client


def trigger_get_request(host, port, uri):
    connection = http.client.HTTPConnection(host, port)
    connection.request("GET", uri)

    response = connection.getresponse()
    data = response.read()

    return data.decode("utf-8")
