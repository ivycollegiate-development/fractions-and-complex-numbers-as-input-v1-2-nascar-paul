#
try:
    from fractions import Fraction
    a = Fraction (input("Please input a fraction, ex: 3/4 "))
    print(a)
except ZeroDivisionError:
    print('Invaid operation. You cannot divide by zero')
except ValueError:
    print('Invalid response. Please input a fractional value.')