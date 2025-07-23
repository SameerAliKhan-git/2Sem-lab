# b) Method Overriding Example

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Usage
a = Animal()
d = Dog()
c = Cat()

a.speak()  # Animal speaks
d.speak()  # Dog barks
c.speak()  # Cat meows



