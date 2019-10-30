#!/usr/bin/env python

for i in range(0x0, 0x100):
    print("{} & -0x10 = {}".format(hex(i), i & -0x10))
