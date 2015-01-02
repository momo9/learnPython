__author__ = 'momo9'

import sys

class MyClass:
    i = 100
    def __init__(self, s):
        self.s = s


if __name__ == '__main__':
    print MyClass.i
    c = MyClass('hello')
    o = MyClass('world')
    print c.s, o.s
    print c.i
    c.i = 10
    print o.i
    MyClass.i = 10
    print o.i
    sys.exit(0)
