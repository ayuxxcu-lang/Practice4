# generators.py

# 1. Iterator example
numbers = [1, 2, 3, 4, 5]
my_iter = iter(numbers)

print(next(my_iter))
print(next(my_iter))

# 2. Custom Generator
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()

for value in gen:
    print(value)

# 3. Generator expression
squares = (x*x for x in range(5))

for s in squares:
    print(s)