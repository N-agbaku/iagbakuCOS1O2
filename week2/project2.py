
import cmath
import numpy as np

def quadratic_equ(a, b, c):
    if a == 0:
        print("Equation not possible")
        return
    disc = cmath.sqrt(b**2 - 4*a*c)
    root1 = ((-b + disc)/(2*a))
    root2 = ((-b - disc)/(2*a))
    print(f"The roots of the quadratic are: {root1}, {root2}")


def cubic_equ(a, b, c, d):
    if a == 0:
        print("Equation not possible")
        return
    coefficients = [a, b, c, d]
    roots = np.roots(coefficients)
    print("Roots of the cubic equation:")
    for r in roots:
        print(r)
    

def quartic_equ(a, b, c, d, e):
    if a == 0:
        print("Equation not possible")
        return
    coefficients = [a, b, c, d, e]
    roots = np.roots(coefficients)
    print("Roots of the equation")
    for r in roots:
        print(r)
        

print("Root Finder for Polynomial Equations")
print("1. Quadratic Equation (Ax² + Bx +c)")
print("2. Cubic Equation (ax^3 + bx^2 + cx +d")
print("3. Quartic Equation (ax^4 + bx^3 + cx^2 + dx + e = 0)")

choice = float(input("Pick 1/2/3:"))

if choice == 1:
    a = float(input("Enter coefficient of A:"))
    b = float(input("Enter coefficient of B:"))
    c = float(input("Enter coefficient of C:"))
    quadratic_equ(a, b, c)
    
if choice == 2:
    a = float(input("Enter coefficient of A:"))
    b = float(input("Enter coefficient of B:"))
    c = float(input("Enter coefficient of C:"))
    d = float(input("Enter coefficient of D:"))
    cubic_equ(a, b, c, d)
    
if choice == 3:
    a = float(input("Enter coefficient of A:"))
    b = float(input("Enter coefficient of B:"))
    c = float(input("Enter coefficient of C:"))
    d = float(input("Enter coefficient of D:"))
    e = float(input("Enter coefficient of E"))
    

    