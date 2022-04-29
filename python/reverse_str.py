# extending builtin classes
# through inheritance
# to make work eassier

class ReverseStr(str):
    def __str__(self) -> str:
        return self[::-1]


def main():
    print(ReverseStr("broadways"))


if __name__ == '__main__':
    main()
