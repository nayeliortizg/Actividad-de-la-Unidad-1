from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
from urllib.parse import urlparse, parse_qs


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

def do_GET(self):
    if self.path == '/':
        try:
            with open('home.html', 'r') as file:
                content = file.read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "File Not Found")
    else:
        self.send_error(404, "File Not Found")
    


if __name__ == "__main__":
    print(f"Servidor escuchando en el puerto {server_address[1]}")
    server = HTTPServer(("localhost", 8000), WebRequestHandler) # Cambiando 8080 al puerto 8000
    server.serve_forever()
