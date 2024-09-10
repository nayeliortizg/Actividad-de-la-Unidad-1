from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
from urllib.parse import urlparse, parse_qs


class WebRequestHandler(BaseHTTPRequestHandler):
content_dict = {
    '/': '<html><body><h1>Home Page</h1></body></html>',
    '/proyecto/web-uno': '<html><body><h1>Proyecto: web-uno</h1></body></html>',
    '/proyecto/web-dos': '<html><body><h1>Proyecto: web-dos</h1></body></html>',
    '/proyecto/web-tres': '<html><body><h1>Proyecto: web-tres</h1></body></html>',
}

def do_GET(self):
    response = content_dict.get(self.path, '<html><body><h1>404 Not Found</h1></body></html>')
    self.send_response(200 if self.path in content_dict else 404)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()
    self.wfile.write(response.encode())

    

if __name__ == "__main__":
    print(f"Servidor escuchando en el puerto {server_address[1]}")
    server = HTTPServer(("localhost", 8000), WebRequestHandler) # Cambiando 8080 al puerto 8000
    server.serve_forever()
