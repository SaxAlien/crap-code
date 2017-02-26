#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Sourcecode by Al13n_
    Free for use and edit

    GET ONLY!
    Server do not support POST
    if u want to add support POST - add do_POST(self) method
    and use POST request
    But this is crap

    Do not edit code!
    Edit code only for own risk!
   *=============================*

    Have fun
    Specially for Enot237
        :return:
"""

import BaseHTTPServer
import os
import urllib
from BaseHTTPServer import HTTPServer

import Player, helpers

MP3_PATH = './MP3/'
_player = Player.Player()


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _sendHeaders(self, code, _type='text/html'):
        self.send_response(code)
        self.send_header('Content-type', _type)
        self.end_headers()

    def do_GET(self):
        self.path = str(self.path)
        """
            "Hook" events and processing commands
        """

        if self.path == '/':
            self._sendHeaders(200)
            self.wfile.write('<meta http-equiv="refresh" content="0; url=/HTML/index.html" />')
            return

        elif self.path.startswith('/play'):
            MP3 = urllib.unquote(self.path.split('?')[1])
            _player.play('./MP3/{}'.format(MP3))
            self._sendHeaders(200)
            self.wfile.write(helpers.success("Now Playing: {}".format(MP3)))
            return

        elif self.path == '/stop':
            _player.stop()
            self._sendHeaders(200)
            self.wfile.write(helpers.success("stopped"))
            return

        elif self.path.startswith('/pause'):
            _player.pause()
            self._sendHeaders(200)
            self.wfile.write(helpers.success("paused"))
            return

        if self.path.startswith('/list'):
            self._sendHeaders(200)
            self.wfile.write(helpers.playlist(MP3_PATH))
            return

        else:
            try:
                self.page = open(os.path.abspath(self.path[1:]), 'r').read()
                if self.path.endswith('.css'):
                    self._sendHeaders(200, 'text/css')
                elif self.path.endswith(".js"):
                    self._sendHeaders(200, 'application/javascript')
                else:
                    self._sendHeaders(200)
                self.wfile.write(self.page)
            except IOError:
                self.send_error(404, 'Not Found')


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('0.0.0.0', 8080), Handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt as ex:
        httpd.server_close()
        exit(0)

serv = HTTPServer(('0.0.0.0', 8080))  # , HttpProcessor)
serv.serve_forever()
