from math.add import add

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    if fruit == "Banana":
        continue

    print(fruit)

person = {
    "name": "John",
    "age": 25
}
print("\nFor loop with dictionary:")
for k, v in person.items():
    print(f"{k}: {v}")

name = "Freitz"
hello = f"Hello, {name}"
print(hello)

def person_info(name, age=None, city=None):
    """Function with keyword arguments."""
    return f"{name} is {age} years old from {city}"

print(person_info(name="Ian", city="London"))

def greetv2(*args):
    return f"Hello, {args[0]} from {args[1]}!"

print(greetv2("Ian", "London", "UK"))

total = add(5, 10)
print(f"Total from add function: {total}")