#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Crap class
    but make code more compact. lmao

    WARNING! WARNING!
    HIGH CONCENTRATION OF SHIT!

    and in future here will be adding more and more methods and classes
    but i'm not shure
"""

import os


def success(message):
    return '<div class="alert alert-success alert-dismissable">' \
           '<button type="button" class="close" data-dismiss="alert">&times;</button>' \
           '{}</div>'.format(message)


def warning(message):
    return '<div class="alert alert-danger alert-dismissable">' \
           '<button type="button" class="close" data-dismiss="alert">&times;</button>' \
           '{}</div>'.format(message)


def playlist(path):
    """
        Especially here ._.

    :param path:
    :return:
    """
    listdir = os.listdir(path)
    raw_html = ''
    for i in listdir:
        raw_html += '<option>{}</option>'.format(unicode.encode(unicode(str(i), 'utf-8'), 'utf8'))
    return raw_html  # fix utf-8 encode and some useful stuff such as <option> format
