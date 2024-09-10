from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
from urllib.parse import urlparse, parse_qs


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

def do_GET(self):
    parsed_url = urlparse(self.path)
    path = parsed_url.path
    query_params = parse_qs(parsed_url.query)
    autor = query_params.get('autor', ['desconocido'])[0]

    if path == '/proyecto/web-uno':
        response = f"<h1>Proyecto: web-uno Autor: {autor}</h1>"
    else:
        response = "<h1>404 Not Found</h1>"

    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()
    self.wfile.write(response.encode())

    


if __name__ == "__main__":
    print(f"Servidor escuchando en el puerto {server_address[1]}")
    server = HTTPServer(("localhost", 8000), WebRequestHandler) # Cambiando 8080 al puerto 8000
    server.serve_forever()
