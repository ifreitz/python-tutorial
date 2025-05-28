class Person:
    """Basic class example."""
    
    def __init__(self, name, age, gender=None):
        self.name = name
        self.age = age
        self.gender = gender
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def get_age(self):
        return self.age

person = Person("John", 25)

print(person.greet())
print(f"Name: {person.name}")