#!/usr/bin/env python2.6
import sys
import cjson
from spidermonkey import Runtime
import re

rt = Runtime()
cx = rt.new_context()
cx.eval_script('r=[];')

#print "Loading jsonpath..."
with file('jsonpath.js') as f:
    cx.eval_script(f.read())

#print "Parsing json from stdin..."
cx.eval_script("i=%s;" %sys.stdin.read()) # for (j in i){ n=i[j]; r.push(%s); }" % (sys.stdin.read(), sys.argv[1]))

r = cx.eval_script("jsonPath(i, '%s');" % sys.argv[1].replace('\'', '"'))
for line in r:
    print line

