#program to solve the quadratic equation
#Date: 20/02/24
#Name:Tracy Kanyora
import math

a =float(input("enter the coefficient of first term : "))
b =float (input("enter the coefficient of second term : "))
c =float (input("enter the constant : "))

d = (b**2) - 4 * a * c
x_1 = (-b + math . sqrt (d) ) / 2* a 
x_2 = (-b - math . sqrt (d) ) / 2* a 

print(" The first solution of the quadratic equation" , x_1)
print(" The second solution of the quadratic equation", x_2)


