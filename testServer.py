from http.server import BaseHTTPRequestHandler, HTTPServer

class TestServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("pinged")

def run(server_class=HTTPServer, handler_class=TestServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Server started')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')

if __name__ == "__main__":
    run()
