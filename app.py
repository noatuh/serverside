from http.server import BaseHTTPRequestHandler, HTTPServer

class Redirect(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set HTTP response status code to 301 (permanent redirect)
        self.send_response(301)
        self.send_header("Location", "https://noatuh.github.io/public-site/")
        self.end_headers()

if __name__ == "__main__":
    server_address = ("", 80)  # Serve on port 80
    httpd = HTTPServer(server_address, Redirect)
    print("Serving on port 80...")
    httpd.serve_forever()
