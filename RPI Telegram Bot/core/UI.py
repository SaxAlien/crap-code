#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 UserInterface module for Telegram
 Now here only keyboard, but in future, im hope, here will be more UI stuff
 eg: TouchPanel or other stuff
"""

from telebot import types

status =\
"""
<pre>  ===== Status =====</pre>
    PC state: <i>{}</i>
    Relay state: <i>{}</i>
    Verbose: <i>{}</i>
    Watchdog: <i>{}</i>
    TK state: <i>N/A</i>
"""

def show_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Turn light')
    keyboard.add('Turn PC')
    keyboard.add('Status', 'Verbose', 'Watchdog')
    return keyboard


def hide_keyboard():
    return types.ReplyKeyboardRemove()
