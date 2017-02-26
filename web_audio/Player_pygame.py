#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    ToDo: Fix That Shit

    Sourcecode powered By: juehan
    GitHub: https://gist.github.com/juehan/1869090
    Edited By Al13n_
"""

import pygame
import threading


class Player():
    # Dahmn shit
    # But in future will be fixed, i'm hope
    def __init__(self):
        pygame.init()
        BUFFER = 3072  # 3072
        FREQ, SIZE, CHAN = pygame.mixer.get_init()
        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
        self.state = False
        self.is_paused = False

    def playProcessed(self, file):
        self.state = True
        clock = pygame.time.Clock()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(1000)

    def play(self, file):
        if self.state:
            self.stop()
        _ = threading.Thread(target=self.playProcessed, args=(file,))
        _.start()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        if not self.is_paused:
            self.is_paused = True
            self._pause()
            return
        self.is_paused = False
        self._unpause()

    def _pause(self):
        pygame.mixer.music.pause()

    def _unpause(self):
        pygame.mixer.music.unpause()
