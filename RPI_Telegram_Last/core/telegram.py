#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Telegram module, core of a bot

"""

# ToDo: add music player
# ToDo: add RPi controls & status

import telebot
import helpers
import ui
import gpio
from threading import Thread
from time import sleep

bot = telebot.TeleBot(helpers.token)
err = '\xf0\x9f\x98\xa3'
ok = '\xf0\x9f\x98\x89'
verbose = True
watchdog = False


def convert(state):
    if state:
        return 'Enabled'
    return 'Disabled'


def send_message(msg):
    bot.send_message(helpers.admin_uid, msg, parse_mode='HTML')


def _watchdog():
    global watchdog
    while watchdog:
        if helpers.is_pc_up():
            send_message('Hey! PC now is Up and ready for use!\n\nWatchdog now is disabled {}'.format(ok))
            break
        sleep(1)
    watchdog = False


@bot.message_handler(commands=['menu', 'start', 'show', 'm'])
def _(msg):
    if msg.chat.id != helpers.admin_uid: return
    helpers.log('message_handler', 'Call menu from {}'.format(msg.chat.id))
    bot.reply_to(msg, 'Welcome <3', reply_markup=ui.show_keyboard())


@bot.message_handler(commands=['hide'])
def _(msg):
    if msg.chat.id != helpers.admin_uid: return
    bot.reply_to(msg, ok, reply_markup=ui.hide_keyboard())


@bot.message_handler(content_types=['text'])
def _(msg):
    if msg.chat.id != helpers.admin_uid: return

    global verbose, watchdog
    if msg.text == 'Status':
        bot.reply_to(msg,
                     ui.status.format(
                         convert(gpio.get_state(gpio.relay_pin1)),
                         convert(gpio.get_state(gpio.relay_pin2)),
                         convert(gpio.get_state(gpio.relay_pin3)),
                         convert(gpio.get_state(gpio.relay_pin4)),
                         convert(helpers.is_pc_up()),
                         convert(verbose),
                         convert(watchdog)
                     ),
                     parse_mode='HTML')
        return

    if msg.text == 'Turn PC':
        if helpers.is_pc_up():
            if not (gpio.get_state(gpio.relay_pin1) and
                        gpio.get_state(gpio.relay_pin2) and
                        gpio.get_state(gpio.relay_pin3)):
                bot.reply_to(msg, 'Relays already off')
                return
            gpio.hold_off(gpio.relay_pin1)
            gpio.hold_off(gpio.relay_pin2)
            gpio.hold_off(gpio.relay_pin3)
            gpio.hold_off(gpio.relay_pin4)
            bot.reply_to(msg, 'Turning off relays')
        else:
            bot.reply_to(msg, 'Turning on PC')
            gpio.hold_on(gpio.relay_pin1)
            sleep(0.3)
            gpio.hold_on(gpio.relay_pin2)
            sleep(0.3)
            gpio.hold_on(gpio.relay_pin3)
            sleep(1)
            gpio.push(gpio.pc_pin)
        return

    if msg.text == 'Turn light':
        if gpio.get_state(gpio.relay_pin4):
            gpio.hold_off(gpio.relay_pin4)
        else:
            gpio.hold_on(gpio.relay_pin4)
        bot.reply_to(msg, 'Light now is <i>{}</i>'.format(convert(gpio.get_state(gpio.relay_pin4))), parse_mode='HTML')
        return

    if msg.text == 'Verbose':
        if not verbose:
            verbose = True
        else:
            verbose = False
        bot.reply_to(msg, 'Verbose mode: <i>{}</i>'.format(convert(verbose)), parse_mode='HTML')
        return

    if msg.text == 'Watchdog':
        if helpers.is_pc_up():
            bot.reply_to(msg, 'Seems what PC already On.. {}'.format('\xf0\x9f\x98\xb3'))
            return
        if not watchdog:
            watchdog = True
            # Sorry me God for that..
            Thread(target=_watchdog, args=()).start()
        else:
            watchdog = False
        bot.reply_to(msg, 'Watchdog mode: <i>{}</i>'.format(convert(watchdog)), parse_mode='HTML')

    helpers.log('message_handler', u'Receive message from {} | Text: {}'.format(msg.chat.id, msg.text))


def Start():
    helpers.log('Start()', 'Run Start() function at core.telegram')
    try:
        bot.polling(True)
    except Exception as ex:
        helpers.log('Start()', 'Crash Start() function in core.telegram ({})\n\n{}'.format(__file__, ex), True)
