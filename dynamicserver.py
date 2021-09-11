#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
import os

#
# CORS supporting server from SO:
# https://stackoverflow.com/a/21957017
#
class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        if hasattr(self,"datafile"):
          self.send_header('datafile', self.datafile)
        SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        if self.path == "/latest":
          datafiles = [d for d in os.listdir() if d[-4:] == ".txt"]
          datafiles.sort()
          last = datafiles[-1]
          self.path = "/"+last
          self.datafile = last

        SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
