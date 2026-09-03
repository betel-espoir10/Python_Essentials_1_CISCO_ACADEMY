#Shadow methods are methods that are defined in a subclass with the same name as a method in the superclass. When a subclass defines a method with the same name as a method in its superclass, the subclass's method "shadows" or "overrides" the superclass's method. This means that when you call the method on an instance of the subclass, the subclass's version of the method will be executed instead of the superclass's version.

def message(number):
    print("\nEnter a number:", number)
 
number = 1234
message(200)
print(number)

# Using multiple parameters in a function
def self_introduction(name, age, city):
    print("\nHello! My name is", name)
    print("I am", age, "years old")
    print("I live in", city)

self_introduction("Alice", 30, "New York")

#using keyword arguments passing values to a function
def self_introduction(name, age, city):
    print("\nHello! My name is", name)
    print("I am", age, "years old")
    print("I live in", city)

self_introduction(name="Bob-lengar", age=25, city="Moundou")
self_introduction(city="Doba", name="Charline", age=35)

#Using default parameter values in a function
def self_introduction(name, age=18, city="Kelo"):
    print("\nHello! My name is", name)
    print("I am", age, "years old")
    print("I live in", city)
self_introduction("David Gonbeloum")