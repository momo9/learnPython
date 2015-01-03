__author__ = 'momo9'

def gen(n):
    for i in xrange(10):
        yield i * n

if __name__ == '__main__':
    for i in gen(2):
        print i

    print 'sum:', sum(gen(2))
    print 'sum:', sum(i * 2 for i in xrange(3))