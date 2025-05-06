# Python Basics I: Variables, Data Types, and Conditionals

# -------------------------------------
# 📝 COMMENTS
# This is a single-line comment

"""
This is a multi-line comment.
Useful for explanations or documentation.
sadsa
asdasd
asdasd
"""

# -------------------------------------
# 🔠 VARIABLES & NAMING CONVENTIONS
# Use snake_case and descriptive names

user_name = "Ian"
user_age = 20
is_member = True

# -------------------------------------
# 📊 DATA TYPES
price = 99.99                 # float
is_valid = True               # boolean
names = ["Ian", "Edchel", True]     # list
count = 5                     # int

# Dictionary (Mapping)
profile = {
    "name": "Ian",                 # string
    "age": 20,                     # int
    "is_married": False,          # bool
    "cats": ["Ed", "Kala"]        # list
}

name = profile["name"]
age = profile["age"]
cats = profile["cats"]

name = profile.get("name")

# ["Ed", "Kala"]
# "Kala"

excel_data = [
    {
        "name": None,
        "age": 29
    },
    {
        "name": "Ian",
        "age": 30
    },
    {
        "age": 30
    },
    {
        "name": "Ian",
        "age": 30
    }
]



# -------------------------------------
# 🔍 TYPE CHECKING
print(type(user_name))   # <class 'str'>
print(type(price))       # <class 'float'>

# -------------------------------------
# 🔁 TYPE CASTING
age_as_str = str(user_age)  # convert int to str
price_as_int = int(price)   # convert float to int
price_as_float = float(price_as_int)

# -------------------------------------
# ⌨️ OPTIONAL: USER INPUT
# name_input = input("Enter your name: ")
# print(f"Hello, {name_input}!")

# -------------------------------------
# ✅ CONDITIONALS

# Check age
if profile["age"] >= 18:
    print(f"{profile['name']} is an adult.")
    values = 6
    print("Value")
else:
    print(f"{profile['name']} is a minor.")

# Check marital status
if profile["is_married"]:
    print(f"{profile['name']} is married.")
else:
    print(f"{profile['name']} is not married.")

# Check list membership
if "Kala" in profile["cats"]:
    print("Kala is one of the cats.")

# Combine conditions
if is_valid and price < 100:
    print("The item is valid and affordable.")
