import cmath
a = 2
b = 4
c = 6
# calculate the discriminant
d = (b ** 2) - (4 * a * c)
neg = (-b - cmath.sqrt(d)) / (2 * a)
pos = (-b + cmath.sqrt(d)) / (2 * a)
print("The solution are {0} and {1}".format(neg, pos))