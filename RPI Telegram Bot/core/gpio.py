#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 GPIO module
 Only for easily use and clean-code (and still looks crappy..)
"""

import helpers, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pc_pin = 4

relay_pin1 = 26 # monitor
relay_pin2 = 19 # pc
relay_pin3 = 13 # sound
relay_pin4 = 06 # light

out = [pc_pin, relay_pin1, relay_pin2, relay_pin3, relay_pin4]
for i in out: GPIO.setup(i, GPIO.OUT); GPIO.output(i, GPIO.LOW)

def clean():
    GPIO.cleanup()


def get_state(pin):
    return bool(GPIO.input(pin))


def hold_off(pin):
    GPIO.output(pin, False)


def push(pin):
    GPIO.output(pin, True)
    time.sleep(0.5)
    GPIO.output(pin, False)


def hold_on(pin):
    GPIO.output(pin, True)
    time.sleep(1)


def turn_on():
    try:
        hold_on(5);
        push(4)
    except Exception as ex:
        helpers.log('Turn_On()', 'Crash Turn_On() function in core.gpio ({})\n\n{}'.format(__file__, ex), True)


def turn_off():
    try:
        hold_off(5)
    except Exception as ex:
        helpers.log('Turn_Off()', 'Crash Turn_Off() function in core.gpio ({})\n\n{}'.format(__file__, ex), True)
