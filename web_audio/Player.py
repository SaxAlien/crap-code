#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    ToDo: add more functions
    By Al13n_
"""

from subprocess import Popen, PIPE
from threading import Thread
import time


class Player():
    def __init__(self):
        self.is_alive = False
        self.player = None

    def playProcessed(self, file):
        self.player = Popen(["/usr/bin/mplayer", "-quiet", file], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self.is_alive = True
        while self.player.poll()==None:
            time.sleep(.3)
        self.is_alive = False

    def play(self, file):
        if self.is_alive:
            self.stop()
            Thread(target=self.playProcessed, args=(file,)).start()
        else:
            Thread(target=self.playProcessed, args=(file,)).start()
        return True

    def stop(self):
        if self.is_alive:
            self.player.stdin.write('q')
            return True
        return False

    def pause(self):
        if self.is_alive:
            self.player.stdin.write('p')
            return True
        return False
