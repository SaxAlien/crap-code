#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Help module. Contains methods are not important for work and some settings, eg token, admin uid..
 AND U SEE ALL OF THEM
 In future will be added more functions, may be :3
"""

from __future__ import print_function
import socket
from threading import Lock, Thread
from datetime import datetime

# import os
# import random
# import string

token = '205815783:AAFw-8r6MxcAUNPQKuK5IcLwsviH-lZPUeA'
admin_uid = 134771371
pc_address, pc_service = '192.168.0.100', 22  # IP and service for startup detect

print_lock = Lock()

"""
def get_image():
    path = gen_random()
    os.system('fswebcam -r 1280x720 --no-banner {} > /dev/null 2>&1'.format(path))
    return path


def gen_random(lenght=15):
    return '/tmp/{}.jpg'.format(''.join(random.sample(string.ascii_uppercase + string.digits * 6, lenght)))
"""




def is_pc_up():
    try:
        _ = socket.socket()
        _.connect((pc_address, pc_service))
        _.close()
        return True
    except socket.error:
        return False


def log(event, data, error=False):
    # ToDo: logging in file
    with print_lock:
        pattern = '\x1b[36m'
        if error: pattern = '\x1b[91m'
        print(u'[ \x1b[37m{}\033[0m ] [{}: {} :\033[0m] \t > \t {}'.format(datetime.now(), pattern, event, data))
