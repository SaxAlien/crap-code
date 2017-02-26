#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telebot import types

status = \
    """
    <pre>  ===== Status =====</pre>
        Relay1 state: <i>{}</i>
        Relay2 state: <i>{}</i>
        Relay3 state: <i>{}</i>
        Relay4 state: <i>{}</i>
        PC state: <i>{}</i>
        Verbose: <i>{}</i>
        Watchdog: <i>{}</i>
        TK state: <i>N/A / pizda</i>
    """


def show_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Turn light')
    keyboard.add('Turn PC')
    keyboard.add('Status', 'Verbose', 'Watchdog')
    return keyboard


def hide_keyboard():
    return types.ReplyKeyboardRemove()
