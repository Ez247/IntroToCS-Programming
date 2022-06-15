"""Using Floats:
        0. We need to first understand binary numbers.
            a. A binary number is represented by a sequence of digits each of which is either 0 or 1.
            b. These digits are of ten called bits.
        1. Floating point: non-integer numbers. 
"""


x = 0.0
for i in range(10):
    x += 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')
