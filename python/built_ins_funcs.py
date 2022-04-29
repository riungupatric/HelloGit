
def reversing(sen):
    # reversed() returns an iterator
    new = reversed(sen.split())
    for word in new:
        print(f"{word} ", end="")
    print()


def any_truth(container):
    # returns true if at least one of the
    # items in the container evaluates to true
    print(any(container))  # print true of false


def all_true(container):
    # everything in the container must be true
    print(all(container))


def zipper(students, marks):
    # combine two containers and returns tuple
    # sort marks in descending order
    for name, points in zip(students, sorted(marks, reverse=True)):
        print(f"{name} : {points}")


def enumerator(container):
    # sort container(marks) in descending order
    for index, name in enumerate(container):
        print(f"{index} : {name}")


def main():
    mantra = "simple is better than complex"
    students = ['paul', 'leo', 'ian', 'alan', 'joe', 'joy']
    marks = [12, 30, 40, 50, 40, 0]
    reversing(mantra)
    any_truth(marks)
    all_true(marks)
    zipper(students, marks)
    enumerator(students)


if __name__ == '__main__':
    main()
