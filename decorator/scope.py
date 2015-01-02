__author__ = 'momo9'

s = []

def foo():
    s = []
    s.append(1)
    print s

def bar(x):
    s.append(x)
    print s

if __name__ == "__main__":
    s.append(0)
    print s
    foo()
    s.append(2)
    print s
    s = []
    s.append(3)
    print s
    bar(10)