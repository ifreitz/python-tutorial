"""
Python Basics II - Loops, Functions, Modules, and Classes
This file demonstrates key concepts in Python programming.
"""

# ===== LOOPS =====
print("\n=== Loops Examples ===")

# For loop with range
print("\nFor loop with range:")
for i in range(5):
    print(f"Count: {i}")  # Prints 0 to 4

# For loop with list
fruits = ["apple", "banana", "cherry"]
print("\nFor loop with list:")
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with dictionary
person = {"name": "John", "age": 25}
print("\nFor loop with dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(f"While count: {count}")
    count += 1

# Loop control statements
print("\nLoop control statements:")
for i in range(5):
    if i == 2:
        continue  # Skip 2
    if i == 4:
        break    # Stop at 4
    print(f"Number: {i}")
else:
    print("Loop completed normally")

# ===== FUNCTIONS =====
print("\n=== Functions Examples ===")

def greet(name):
    """Basic function with a single parameter."""
    return f"Hello, {name}!"

def calculate_area(length, width=10):
    """Function with default parameter."""
    return length * width

def person_info(name, age, city):
    """Function with keyword arguments."""
    return f"{name} is {age} years old from {city}"

def sum_all(*args):
    """Function with variable arguments."""
    return sum(args)

def get_dimensions():
    """Function with multiple return values."""
    return 5, 10

# Test functions
print(greet("Alice"))
print(f"Area: {calculate_area(5)}")
print(person_info(name="John", age=25, city="New York"))
print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
length, width = get_dimensions()
print(f"Dimensions: {length}x{width}")

# ===== CLASSES =====
print("\n=== Classes Examples ===")

class Person:
    """Basic class example."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Math:
    """Class demonstrating class and static methods."""
    
    @classmethod
    def add(cls, x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

class Animal:
    """Base class for animals."""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"
    
    def __str__(self):
        return f"{self.name} is an animal"

class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return "Woof!"
    
    def __str__(self):
        return f"{self.name} is a {self.breed} dog"

# Test classes
person = Person("John", 25)
print(person.greet())

print(f"Math.add(5, 3): {Math.add(5, 3)}")
print(f"Math.multiply(4, 2): {Math.multiply(4, 2)}")

dog = Dog("Buddy", "Golden Retriever")
print(dog)
print(f"Sound: {dog.speak()}")

# ===== MODULES =====
print("\n=== Modules Example ===")
print("Note: To use modules, create separate files and import them.")
print("Example module structure:")
print("""
math_operations.py:
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y

main.py:
    from math_operations import add, subtract
    
    result = add(5, 3)
    print(result)  # Output: 8
""") 