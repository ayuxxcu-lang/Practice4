import math

# 1. Convert degree to radian
degree = 15
radian = degree * (math.pi / 180)
print("1) Degree to Radian")
print("Input degree:", degree)
print("Output radian:", round(radian, 6))


# 2. Area of trapezoid
height = 5
base1 = 5
base2 = 6
trapezoid_area = 0.5 * (base1 + base2) * height

print("\n2) Area of Trapezoid")
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", trapezoid_area)


# 3. Area of regular polygon
n = 4
side = 25
polygon_area = (n * side ** 2) / (4 * math.tan(math.pi / n))

print("\n3) Area of Regular Polygon")
print("Input number of sides:", n)
print("Input the length of a side:", side)
print("The area of the polygon is:", round(polygon_area))


# 4. Area of parallelogram
base = 5
height_para = 6
parallelogram_area = base * height_para

print("\n4) Area of Parallelogram")
print("Length of base:", base)
print("Height of parallelogram:", height_para)
print("Expected Output:", float(parallelogram_area))