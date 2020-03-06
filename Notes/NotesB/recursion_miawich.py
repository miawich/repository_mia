# recursion - 03/05/20


def f():
    print("f")


def g():
    print("g")
    f()
    g()
    print("END")


g()


def controlled(depth):
    print("recursion depth", depth)
    if depth > 0:
        controlled(depth - 1)
        print("recursion depth", depth, "has closed")
