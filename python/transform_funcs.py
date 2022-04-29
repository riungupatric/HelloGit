# built-in functions to tranform data

from curses.ascii import isupper
from math import sqrt


def filter_lowers(x):
    if isupper(x):
        return False
    else:
        return True


def filter_odds(x):
    if x % 2 == 0:
        return False
    else:
        return True


def square_grades(x):
    return x**2


def letter_grades(x):
    if x >= 80:
        return 'A'
    elif x >= 75:
        return 'A-'
    elif x >= 65:
        return 'B+'
    elif x >= 60:
        return 'B'
    elif x >= 55:
        return 'B-'
    else:
        return 'C'


def main():
    # data
    grades = [89, 85, 74, 23, 45, 60, 57, 45]
    chars = 'abcdEFGHijklMNOPqrsTUVz'
    numbers = [1, 2, 3, 4, 5, 76, 8, 34, 5, 7, 89, 12, 56]

    # working on data
    # functions that take a callback function
    odds = list(filter(filter_odds, numbers))
    # print(odds)

    # filter lowers
    lowers = list(filter(filter_lowers, chars))
    # print(lowers)

    # square grades
    squared = list(map(square_grades, grades))
    # print(squared)

    # grades to letters
    grds = sorted(grades, reverse=True)
    ranks = list(map(letter_grades, grds))
    print(ranks)


if __name__ == '__main__':
    main()
