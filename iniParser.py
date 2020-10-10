#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

re_comment = r'(?P<comment>;.*$)'
re_section = r'\[(?P<section>.*)\['
re_keyval = r'(?P<key>[\w]*)=(?P<val>[\w\\\s/:])'


def parse(filename):

    with open(filename, 'r'):
        lines = filename.readlines()

    for line in lines:

        current_section = ''

        if re.match(re_comment, line):
            current_comment += line
        elif re.match(re_section, line):
            current_section =


