from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

def do_GET(self):
    # Registro de datos de la solicitud
    host = self.headers.get('Host')
    user_agent = self.headers.get('User-Agent')
    path = self.path

    # Preparar respuesta
    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.send_header('Server', 'SimpleHTTPServer')
    self.send_header('Date', self.date_time_string())
    self.end_headers()

    # Registro de datos de la respuesta
    content_type = 'text/html'
    server = 'SimpleHTTPServer'
    date = self.date_time_string()

    print(f"Request Headers:\nHost: {host}\nUser-Agent: {user_agent}\nPath: {path}")
    print(f"Response Headers:\nContent-Type: {content_type}\nServer: {server}\nDate: {date}")

    # Enviar respuesta
    self.wfile.write(b"<html><body><h1>Hola Mundo by Nayeli Ortiz Garcia 21210406</h1></body></html>")

    


if __name__ == "__main__":
    print(f"Servidor escuchando en el puerto {server_address[1]}")
    server = HTTPServer(("localhost", 8000), WebRequestHandler) # Cambiando 8080 al puerto 8000
    server.serve_forever()
