class Animal:
    def moves(self):
        print("Animal is moving")

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def barks(self):
        print("Dog is barking")

    def play(self):
        print("Dog is playing")


class Cat(Animal):
    # Suppose we want to leave this class empty, it only wants to inherit methods
    # So we just write "pass" or it will give error
    pass


dog1 = Dog()
dog1.play()
dog1.barks()
dog1.eat()
dog1.moves()