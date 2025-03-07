from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"message": "OK"}') #Example response
    def do_POST(self):
        if self.path == '/register':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            #self.wfile.write(b'{"message": "OK"}')
            self.wfile.write(b'{"id":4,"token":"QpwL5tke4Pnpja7X4"}')
        if self.path == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            #self.wfile.write(b'{"message": "OK"}')
            self.wfile.write(b'{"token":"QpwL5tke4Pnpja7X4"}')
        if self.path == '/create-case':
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"caseId": "98765EBD27Z0T56"}')
    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"message": "OK"}')
    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"message": "OK"}')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

