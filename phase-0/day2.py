# ============================================================
# Day 2 - OOP, Comprehensions, File I/O, Error Handling
# ============================================================

# Exercise 1 - OOP and Inheritance
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

animal = Animal("Cat", "Meow")
dog = Dog("Buddy", "Woof")
animal.speak()  # Cat says Meow
dog.speak()     # Buddy barks!


# Exercise 2 - List Comprehension
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


# Exercise 3 - Dict Comprehension
sentence = "machine learning is amazing"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)
# {'machine': 7, 'learning': 8, 'is': 2, 'amazing': 7}


# Exercise 4 - File I/O
with open("test.txt", "w") as f:
    f.write("I am Avinash\nI am learning AI and ML\nThis is day 2")

def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

read_file("test.txt")
# I am Avinash
# I am learning AI and ML
# This is day 2


# Exercise 5 - Error Handling
def check_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    if value < 0:
        raise ValueError("Input cannot be negative")
    return value

test_values = [-5, "hello", 10]
for val in test_values:
    try:
        print(check_number(val))
    except Exception as e:
        print(f"Error for {val}: {e}")
# Error for -5: Input cannot be negative
# Error for hello: Input must be a number
# 10