#!/usr/bin/env python

# wsgi app

def app(environ, start_response):
    response_body = "Hello World"

    header = [('Content-Type', 'text/html')]
    status = "200 OK"

    start_response(status, header)

    print("environ http request method:" + environ['REQUEST_METHOD'])

    return [response_body]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    httpd = make_server("0.0.0.0", 8081, app)
    print("httpd run on: " + str(httpd.server_port))
    httpd.serve_forever()