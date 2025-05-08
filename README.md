# Python Basics I & II

## Python Basics I - Variables, Data Types, and Conditionals

Welcome to the first lesson of Python Basics! In this tutorial, you'll learn the core concepts of Python programming: variables, data types, type checking, type casting, and conditionals. This lesson is beginner-friendly and provides hands-on code examples.

---

## 🧠 What You'll Learn in Python Basics I

### 1. Variables and Data Types

#### Variables
Variables are containers for storing data values. In Python, variables are created when you assign a value to them. Python is dynamically typed, meaning you don't need to declare the type of a variable when you create it.

```python
# Variable assignment
name = "John"      # String variable
age = 25          # Integer variable
height = 1.75     # Float variable
is_student = True # Boolean variable
```

#### Data Types
Python has several built-in data types:

1. **Integers (`int`)**
   - Whole numbers, positive or negative
   - No decimal point
   - Example: `5`, `-3`, `1000`

2. **Floating-point numbers (`float`)**
   - Numbers with decimal points
   - Can be positive or negative
   - Example: `3.14`, `-0.001`, `2.0`

3. **Strings (`str`)**
   - Text enclosed in quotes (single or double)
   - Can contain letters, numbers, and special characters
   - Example: `"Hello"`, `'Python'`, `"123"`

4. **Booleans (`bool`)**
   - Represents True or False
   - Used in conditional statements
   - Example: `True`, `False`

5. **Lists (`list`)**
   - Ordered, mutable collections
   - Can contain mixed data types
   - Example: `[1, "hello", 3.14]`

6. **Dictionaries (`dict`)**
   - Key-value pairs
   - Unordered, mutable
   - Example: `{"name": "John", "age": 25}`

### 2. Type Checking and Casting

#### Type Checking
The `type()` function is used to check the data type of a variable:

```python
x = 5
print(type(x))  # Output: <class 'int'>

name = "John"
print(type(name))  # Output: <class 'str'>
```

#### Type Casting
Type casting is the process of converting one data type to another:

1. **`int()`**: Converts to integer
   ```python
   x = int(3.14)    # Result: 3
   y = int("123")   # Result: 123
   ```

2. **`float()`**: Converts to float
   ```python
   x = float(3)     # Result: 3.0
   y = float("3.14") # Result: 3.14
   ```

3. **`str()`**: Converts to string
   ```python
   x = str(123)     # Result: "123"
   y = str(3.14)    # Result: "3.14"
   ```

4. **`bool()`**: Converts to boolean
   ```python
   x = bool(1)      # Result: True
   y = bool(0)      # Result: False
   ```

### 3. Conditionals

Conditional statements are used to make decisions in code based on certain conditions.

#### If-elif-else Statements
```python
age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Just became an adult")
else:
    print("Adult")
```

#### Comparison Operators
- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

#### Logical Operators
- `and`: Both conditions must be True
- `or`: At least one condition must be True
- `not`: Reverses the boolean value

#### Membership Operators
- `in`: Checks if a value exists in a sequence
- `not in`: Checks if a value doesn't exist in a sequence

---

## Python Basics II - Loops, Functions, Modules, and Classes

Welcome to the second lesson of Python Basics! In this tutorial, you'll learn about more advanced Python concepts: loops, functions, modules, and classes. These concepts are fundamental to writing organized and reusable code.

---

## 🧠 What You'll Learn in Python Basics II

### 1. Loops

Loops are used to execute a block of code multiple times.

#### For Loops
For loops iterate over a sequence (list, tuple, string, etc.):

```python
# Iterating over a range
for i in range(5):
    print(i)  # Prints 0 to 4

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a dictionary
person = {"name": "John", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")
```

#### While Loops
While loops execute as long as a condition is True:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

#### Loop Control Statements
- `break`: Exits the loop
- `continue`: Skips the rest of the current iteration
- `else`: Executes when the loop finishes normally

### 2. Functions

Functions are reusable blocks of code that perform specific tasks.

#### Function Definition
```python
def greet(name):
    return f"Hello, {name}!"
```

#### Parameters and Arguments
1. **Required Parameters**
   ```python
   def add(x, y):
       return x + y
   ```

2. **Default Parameters**
   ```python
   def greet(name, greeting="Hello"):
       return f"{greeting}, {name}!"
   ```

3. **Keyword Arguments**
   ```python
   def person_info(name, age, city):
       return f"{name} is {age} years old from {city}"
   
   # Can be called with keyword arguments
   person_info(name="John", age=25, city="New York")
   ```

4. **Variable Arguments**
   ```python
   def sum_all(*args):
       return sum(args)
   ```

#### Return Values
- Single return: `return value`
- Multiple returns: `return value1, value2`
- No return: Function returns `None`

#### Lambda Functions
Anonymous functions defined with the `lambda` keyword:
```python
square = lambda x: x ** 2
```

### 3. Modules

Modules are Python files containing reusable code.

#### Creating Modules
```python
# math_operations.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

#### Importing Modules
```python
# Import entire module
import math_operations

# Import specific functions
from math_operations import add, subtract

# Import with alias
import math_operations as mo
```

#### Module Organization
- Use `__init__.py` to mark directories as Python packages
- Organize related functions in the same module
- Use clear, descriptive names for modules

### 4. Classes and Object-Oriented Programming

Classes are blueprints for creating objects with properties and methods.

#### Class Definition
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
```

#### Instance Methods and Attributes
- Instance methods: Functions that operate on instance data
- Instance attributes: Variables that belong to instances

#### Class Methods and Static Methods
```python
class Math:
    @classmethod
    def add(cls, x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
```

#### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

#### Special Methods
- `__init__`: Constructor
- `__str__`: String representation
- `__repr__`: Detailed string representation
- `__len__`: Length of object

---

## 📁 File Structure
```bash
python-basics/
│
├── README.md
├── variables_conditionals_example.py
├── loops_functions_classes_example.py
└── math_operations.py
```

---

## ▶️ Running the Examples

### Python Basics I
```bash
python variables_conditionals_example.py
```

Sample output:
```bash
<class 'str'>
<class 'float'>
Ian is an adult.
Ian is not married.
Kala is one of the cats.
The item is valid and affordable.
```

### Python Basics II
```bash
python loops_functions_classes_example.py
```

Sample output:
```bash
=== Loops Examples ===
For loop with range:
Count: 0
Count: 1
Count: 2

For loop with list:
I like apple
I like banana
I like cherry

While loop:
While count: 0
While count: 1
While count: 2

=== Functions Examples ===
Hello, Alice!
Area: 50
Dimensions: 5x10
Square of 4: 16

=== Classes Examples ===
Buddy is a Dog
Sound: Woof!

=== Modules Example ===
Note: To use modules, create separate files and import them.
```

## 🔍 Code Examples

### Variables and Data Types
```python
# Numbers
age = 25          # int
height = 1.75     # float

# Strings
name = "John"     # str
message = 'Hello' # str

# Boolean
is_student = True # bool

# List
fruits = ["apple", "banana", "cherry"]  # list

# Dictionary
person = {
    "name": "John",
    "age": 25
}  # dict
```

### Functions
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def calculate_area(length, width=10):
    return length * width

# Function with multiple returns
def get_dimensions():
    return 5, 10

# Lambda function
square = lambda x: x ** 2
```

### Classes
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
```

### Modules
```python
# math_operations.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# main.py
from math_operations import add, subtract

result = add(5, 3)
print(result)  # Output: 8
```

## 📚 Additional Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Style Guide (PEP 8)](https://peps.python.org/pep-0008/)

