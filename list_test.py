#!/usr/bin/env python
#encoding=UTF-8

import os,sys


for x in [1,2,3]:
    #print x,
    print x
    if x ==2:
        break
    #pass
else:
    print "loop is over"
fn=sys.argv[1]
if not os.path.exists(fn):
    print "%s is not exist" % fn
    sys.exit()

