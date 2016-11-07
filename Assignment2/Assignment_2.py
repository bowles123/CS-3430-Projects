#Brian Bowles, Assignment 2, 01/20/15.

def square(x): return x * x

def cube(x): return square(x) * x

def average(x, y):
    return (x + y) / 2.0

def func1(x):
    return cube(x) - 2.0 * x - 5.0

def func2(x):
    return square(cube(x)) - 2.0

def deriv1(x):
    return 3.0 * square(x) - 2.0

def deriv2(x):
    return 6.0 * cube(x) * square(x)

def next_guess(prev, func, deriv):
    return prev - func(prev) / deriv(prev)

def newton_raphson(guess, func, deriv):
    x = 0.0

    while x != guess:
        x = guess
        guess = next_guess(guess, func, deriv)
        print guess
