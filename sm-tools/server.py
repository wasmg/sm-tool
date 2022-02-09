# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>code with sm</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<a href=""http://codewithsm.c1.biz"">web page </a> ", "utf-8"))
        self.wfile.write(bytes("<br>", "utf-8"))
        self.wfile.write(bytes("<a href=""https://www.tiktok.com/@code_with_sm"">tiktok </a> ", "utf-8"))
        self.wfile.write(bytes("<br>", "utf-8"))
        self.wfile.write(bytes("<a href=""https://www.youtube.com/channel/UCCziiN9AaTlWO7acBDv_O6w"">youtube </a> ", "utf-8"))
        self.wfile.write(bytes("<br>", "utf-8"))
        self.wfile.write(bytes("<a href=""https://github.com/saniya2008sl"">github </a> ", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")