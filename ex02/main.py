from cat import Cat
from animal import Animal
from dog import Dog

def main():
    a = Animal()
    d = Dog()
    c = Cat()
    d.speak()
    c.speak()
    c.sleep()
    d.sleep()
    a.sleep()


if __name__ == '__main__':
    main()