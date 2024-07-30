import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging

class Server(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.end_headers()
    self.wfile.write(bytes('Hello, World!', 'utf-8'))

def run(host, port):
  server = HTTPServer((host, port), Server)
  logging.info('Webserver listening: http://%s:%s', host, port)
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    pass
  server.server_close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Basic web server')
  parser.add_argument('--host', default='0.0.0.0')
  parser.add_argument('--port', default=8000, type=int)
  args = parser.parse_args()
  host = args.host
  port = args.port
  logging.basicConfig(level=logging.INFO, format='%(asctime)s - [my-web-server] - [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

  run(host, port)
