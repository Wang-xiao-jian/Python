#!/usr/bin/python

import os

cmd = 'ping 128.64.6.137'

r = os.popen(cmd)
text = r.read()
r.close()

print(text)