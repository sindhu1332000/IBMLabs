import cmath
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
# calculate the discriminant
d = (b ** 2) - (4 * a * c)
neg = (-b - cmath.sqrt(d)) / (2 * a)
pos = (-b + cmath.sqrt(d)) / (2 * a)
print("The solution are {0} and {1}".format(neg, pos))