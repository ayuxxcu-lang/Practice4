# math.py

import math
import random

# Built-in functions
print(min(3, 7, 1))
print(max(3, 7, 1))
print(abs(-10))
print(round(3.14159, 2))
print(pow(2, 3))

# math module
print(math.sqrt(16))
print(math.ceil(4.2))
print(math.floor(4.9))
print(math.pi)

# random module
print(random.random())
print(random.randint(1, 10))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)