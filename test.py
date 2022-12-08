import math

a = float(input())
factor = 100
# rounding up a decimal to 2 decimal places

num = a * factor
newnum = math.ceil(num)
print(num)
print(newnum/factor)