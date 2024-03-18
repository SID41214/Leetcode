# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


def calculate(a,b):
    m =a*b
    if m <= 1000:
        return m
    
    return a +b
    
    
print(calculate(20,30))
print(calculate(40,30))