#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from string import printable

crypt = '''805eed80cbbccb94c36413275780ec94a857dfec8da8ca94a8c313a8ccf9'''
crypt = [int(crypt[i: i + 2], 16) for i in xrange(0, len(crypt), 2)]

for a in xrange(251):
    for b in xrange(251):
        if (ord('T') * a + b) % 251 == crypt[0] and (ord('W') * a + b) % 251 == crypt[1]:
            flag = ""
            for c in crypt:
                for i in printable:
                    if (ord(i) * a + b) % 251 == c:
                        flag += i

            print flag
