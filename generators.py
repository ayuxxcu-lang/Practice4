def squares_up_to(N):
    for i in range(1, N+1):
        yield i**2


N = 5
for square in squares_up_to(N):
    print(square, end=' ')



def even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))
print(','.join(str(num) for num in even_numbers(n)))



def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 50
for num in divisible_by_3_and_4(n):
    print(num, end=' ')



def squares(a, b):
    for i in range(a, b+1):
        yield i**2

for val in squares(3, 7):
    print(val)



def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num, end=' ')