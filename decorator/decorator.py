__author__ = 'momo9'

def wrapper(fun):
    def decorated(a, b):
        a = 0 if a < 0 else a
        b = 0 if b < 0 else b
        return fun(a, b)
    return decorated

@wrapper
def add(a, b):
    return a + b

if __name__ == '__main__':

    print add(3, 5)
    print add(-3, 1)