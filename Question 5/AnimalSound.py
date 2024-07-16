class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def describe(self):
        print(f"This is a {self.__class__.__name__} named {self.name} and it is {self.age} years old.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow! Meow!")

    def climb(self):
        print(f"{self.name} is climbing the tree!")

class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says: Moo! Moo!")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Tweet! Tweet!")

# Test the program
dog = Dog(name="Buddy", age=3)
dog.describe()
dog.make_sound()
dog.fetch()

cat = Cat(name="Whiskers", age=2)
cat.describe()
cat.make_sound()
cat.climb()

cow = Cow(name="Bessie", age=5)
cow.describe()
cow.make_sound()

bird = Bird(name="Tweety", age=1)
bird.describe()
bird.make_sound()
