# enumerators, for more readable code

from enum import Enum, unique

# make sure enum values are unique
# using unique decorator


@unique
class AnimalRank(Enum):
    COW = 1
    GOAT = 2
    CHICKEN = 3
    RABBIT = 4
    DOG = 5


def main():
    print(AnimalRank.COW)
    print(f"name: {AnimalRank.GOAT.name}, value: {AnimalRank.GOAT.value}")
    print(repr(AnimalRank.CHICKEN))
    print(AnimalRank.DOG.value)

    # enums can also be used as keys
    my_animals = dict()
    my_animals[AnimalRank.DOG] = 'The ultimate protector'
    my_animals[AnimalRank.COW] = 'Milk producer'
    print(AnimalRank.DOG.value)
    print(my_animals)


if __name__ == '__main__':
    main()
