# A decorator is a function that takes another
# function as an argument, adds some functionality
# and then returns another function... working altering
# the original function passed in

from doctest import master
import time


def time_elapse(big_sum):
    def worker():
        start = time.time()
        big_sum()
        stop = time.time()
        print(f"Time elapsed : {(stop - start)*1000} ms")
    return worker

# decorate the big_sum


@time_elapse
def big_sum():
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print(f"The big sum is : {sum(num_list)}")


def main():
    big_sum()


if __name__ == '__main__':
    main()
