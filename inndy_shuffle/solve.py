#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pprint import pprint
import pdb

#  with open("crypted.txt") as f:
    #  s = f.read()
#  #  print len(s)

#  d1 = {}
#  for i in xrange(0x20, 0x7f):
    #  # print chr(i), s.count(chr(i))/float(len(s))
    #  d1[chr(i)] = s.count(chr(i))
#  d1 = sorted(d1.iteritems(), key = lambda x: x[1], reverse=True)
#  #  print d1[: 79]
#  # print "\n\n\n"

#  with open("plain.txt") as f:
    #  s = f.read()
#  d2 = {}

#  l = set(list(s))
#  for i in l:
    #  # print i, s.count(i)/float(len(s))
    #  d2[i] = s.count(i)
#  d2 = sorted(d2.iteritems(), key = lambda x: x[1], reverse=True)
#  #  print d2[30:]
#  #  print d2[30][0]

#  d3 = {}
#  for i, j in zip(d1, d2[:80]):
    #  #  if j[1] == 174:
        #  #  pdb.set_trace()
    #  if i[0] != '\n' and j[0] != '\n':
        #  d3[i[0]] = j[0]
#  #  pprint(d3)
#  print sorted(d3.iteritems(), key = lambda x: x[1])
#  #  print len(d3)

l3 = [('D', ' '), ('\\', 'U'), ('E', '"'), ('O', 'a'), ('%', "'"), ('i', 'q'), ('^', '('), ('w', ','), ('r', 'B'), ('L', '.'), ('K', '/'), (']', 'A'), ('*', '1'), ('s', 'l'), ('H', '3'), ('R', '7'), ('.', 'I'), ('e', 'x'), ('Q', 'C'), ('f', 'F'), ('0', '6'), ('J', ':'), ('j', 'K'), ('#', '@'), ('G', '2'), ('5', '5'), ('<', 'W'), ('+', 'z'), ('{', 'E'), ('2', '9'), ('x', 'j'), ('T', ')'), ('u', '3'), ('c', 'Q'), ('&', '!'), ('|', 'T'), ('~', 'M'), ('v', 'H'), ('o', 'O'), ('y', 'P'), ('A', 'Q'), ('k', 'R'), ('>', '-'), ('h', 'D'), ('9', 'Y'), (' ', 'R'), ('=', 'G'), ('Y', '$'), ('B', 'Z'), ('$', '['), ('S', ']'), ('z', 'a'), ('/', 'b'), ('m', 'c'), (':', 'd'), ('Z', 'e'), ('`', 'f'), ('@', 'g'), ('_', 'h'), ('M', 'i'), ('g', 'N'), ('t', 'k'), ('[', 'l'), ('X', 'm'), ('p', 'n'), ('1', 'o'), ('U', 'p'), ('d', 'J'), ('7', 'r'), ('6', 's'), ('4', 't'), ('N', 'u'), ('W', 'v'), ('?', 'w'), (',', '4'), ('}', 'y'), ('(', 'S'), ('q', '/'), ('8', '}')]
d3 = {}

for i in l3:
    d3[i[0]] = i[1]

with open("crypted.txt") as f:
    s = f.read()
print s[45]
ans = ""
for i in s:
    try:
        ans += d3[i]
    except:
        ans += '\n'
print ans
# # 2 308 ('$', 308), ('S', 308)   ('[', 308), (']', 308)
# 3 51 ('<', 51), ('{', 51), ('~', 51)  ('E', 51), ('M', 51), ('W', 51)
# 2 48 ('x', 48), ('J', 48)  (':', 48), ('j', 48)
# 2 33 ('T', 33), ('^', 33)  (')', 33), ('(', 33)
# 2 30 ('i', 30), ('y', 30)  ('P', 30), ('q', 30)
# 4 1  ('#', 1), ('K', 1), ('B', 1), ('q', 1)  ('/', 1), ('Z', 1), ('{', 1), ('}', 1)

# [('D', ' '), ('\\', '!'), ('E', '"'), ('O', '$'), ('%', "'"), ('i', '('), ('^', ')'), ('w', ','), ('r', '-'), ('L', '.'), ('K', '/'), (']', '0'), ('*', '1'), ('s', '2'), ('H', '3'), ('R', '4'), ('.', '5'), ('e', '6'), ('Q', '7'), ('f', '8'), ('0', '9'), ('J', ':'), ('j', ';'), ('#', '@'), ('G', 'A'), ('5', 'B'), ('<', 'C'), ('+', 'D'), ('{', 'E'), ('2', 'F'), ('x', 'G'), ('T', 'H'), ('u', 'I'), ('c', 'J'), ('&', 'K'), ('|', 'L'), ('~', 'M'), ('v', 'N'), ('o', 'O'), ('y', 'P'), ('A', 'Q'), ('k', 'R'), ('>', 'S'), ('h', 'T'), ('9', 'U'), (' ', 'V'), ('=', 'W'), ('Y', 'Y'), ('B', 'Z'), ('$', '['), ('S', ']'), ('z', 'a'), ('/', 'b'), ('m', 'c'), (':', 'd'), ('Z', 'e'), ('`', 'f'), ('@', 'g'), ('_', 'h'), ('M', 'i'), ('g', 'j'), ('t', 'k'), ('[', 'l'), ('X', 'm'), ('p', 'n'), ('1', 'o'), ('U', 'p'), ('d', 'q'), ('7', 'r'), ('6', 's'), ('4', 't'), ('N', 'u'), ('W', 'v'), ('?', 'w'), (',', 'x'), ('}', 'y'), ('(', 'z'), ('q', '{'), ('8', '}')]
