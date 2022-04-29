# class


class Animal:
    # constructor: object variables
    def __init__(self, **kwargs):
        #self._name = kwargs['name'] if 'name' in kwargs else "Lion"
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    # setter-getter methods

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    # print objects nicely
    def __str__(self) -> str:
        return (f'{self.name()} is a {self.type()} that {self.sound()}')


class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'bird'
        if 'type' in kwargs:
            del kwargs['type']

        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            del kwargs['type']
        self._type = 'mammal'
        super().__init__(**kwargs)

    def play(self, buddy):
        print(f'{self.name()} likes to play with {buddy}')


def animal_details(obj):
    if not isinstance(obj, Animal):
        raise TypeError("animal_details() requires an animal")
    print(f'{obj.name()} is a {obj.type()} that {obj.sound()}')


def main():
    cat = Kitten(name="Cat", sound="meows")
    kiwi = Animal(name="Kiwi", type="bird", sound="qrrrr")
    duck = Duck(name="Goose", sound="qrqrqrqr")

    # animal_details(fish)
    kiwi.name('Hawk')
    print(kiwi)
    print(duck)
    cat.play("rats")


if __name__ == '__main__':
    main()
