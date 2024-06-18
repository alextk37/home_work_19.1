from http.server import BaseHTTPRequestHandler, HTTPServer


class Requests(BaseHTTPRequestHandler):

    def get_html(self):
        with open('index.html', 'r') as html_file:
            text = html_file.read()
        return text

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = self.get_html()
        self.wfile.write(html.encode('utf-8'))


def run():
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Requests)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
