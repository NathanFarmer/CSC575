# J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
#
# This file launches the web server and receives POST requests from search_and_display.js.

import socketserver
import http.server
import logging
import cgi
import json
import sys

PORT = 8000

class ServerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':'text/plain'})
        print(form.getvalue('query'))
        for item in form.list:
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

def euclidean_distance(query):
    return query

if __name__ == '__main__':
    Handler = ServerHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("Serving at port:", PORT)
    httpd.serve_forever()