# variable args list

def main():
    names = ['Patrick', 'Joel', 'Mondi', 'Jefrey']
    attendees(*names)
    details('St. Patrick', 'Programmer', 'Nairobi', 'Kenya')


def attendees(*args):
    if len(args):  # if args length is not zero
        for arg in args:
            print(arg)
    else:
        print("You got stood up, no one attended!")


def details(*args):
    if len(args):
        for arg in args:
            print(arg)
    else:
        print("No details provided!")


if __name__ == '__main__':
    main()
