"""_Newton Raphson:_
        0. The most commonly used approximation algorithm, its typicall called the Newton's Method.
        1. It can be used to find the real roots of many functions.
"""
#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2*guess))
print('Square root of', k, 'is about', guess)
