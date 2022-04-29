# simple intro to classes and objects

class Duck(object):
    sound = "Quaaaaacks!"
    walking = "Walks like a duck!"

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
    bro = Duck()
    bro.quack()
    bro.walk()


if __name__ == '__main__':
    main()
