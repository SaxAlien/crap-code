#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Al13n_ smarthome RPi-based telegram bot, lmao
 Main module, nothing else
"""
# ToDo: add more useful stuff, make more nicely

__version__ = 'r0.3-STABLE'
__author__ = 'Al13n_'
__license__ = None

import core.helpers
import core.telegram


def Main():
    try:
        core.helpers.log('Main()', 'Evoke Main() function', False)
        core.helpers.log('Main()', 'Evoke Start() function in core.telegram', False)
        core.telegram.Start()
    except Exception as ex:
        core.helpers.log('Main()', 'Exception in Main() - {}\n\n{}'.format(__file__, ex), True)
        print(ex)


if __name__ == '__main__':
    Main()
