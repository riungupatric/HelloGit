# Generators are iterators that reurn more than one value

def main():
    # use inclusive_range like real range
    for arg in inclusive_range(1, 5, 0.5):
        print(arg, end=' ')
    print()


def inclusive_range(*args):
    arguments = len(args)
    start = 0
    step = 1

    # instructions
    if arguments < 1:
        raise TypeError(f"Expected at least 1 argument, {arguments} supplied")
    elif arguments == 1:
        stop = args[0]
    elif arguments == 2:
        (start, stop) = args
    elif arguments == 3:
        (start, stop, step) = args
    elif arguments > 3:
        raise TypeError(f"Expected at most 3 arguments, {arguments} supplied")

    # !The Generator
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
    main()
