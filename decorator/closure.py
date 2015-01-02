def acc(n):
    x = [0]
    def plus():
        x[0] += n
        return x[0]
    return plus

if __name__ == '__main__':
    handler1 = acc(1)
    handler3 = acc(3)
    for i in xrange(4):
        print handler1(), handler3()
