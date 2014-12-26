#!/usr/bin/python

import math

def putLine():
    print '=' * 30

if __name__ == '__main__':
    for x in xrange(5):
        print str(x).rjust(4), str(int(math.pow(x, 2))).rjust(4)

    putLine()
    
    for x in xrange(5):
        print '{0:4d} {1:4d} {other}'.format(x, int(math.pow(x, 2)), other='m')

    putLine()
    
    for x in xrange(5):
        print '%4d %4d' % (x, int(math.pow(x, 2)))
