import seaborn as sns
import pandas as pd


"""
Write a recursive function to compute the nth Fibonacci number (sum of previous two numbers within the series starting with 0 and 1).
The fib function is defined as follows:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2) for n > 1
The function should raise a ValueError if the input is not a non-negative integer, which will account for any invalid inputs.
"""

def fib(n):
    if type(n) is int and n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    else:
        raise ValueError("Input must be a non-negative integer")
    
"""
Write a function to convert a non-negative integer to its binary representation as a string.
If the number is 0, the function will automatically return 0.
While the current number is greater than 0, add the remainer of the number when divided by 2 to the binary string and find the new number (which is the current number divided by 2 using the floor division operator (aka the divided number down)).
Once the number is 0, return the found converted binary string.
The function should raise a ValueError if the input is not a non-negative integer, which will account for any invalid inputs.
"""
def to_binary(num):
    binary_string = ""
    if type(num) is int and num >= 0:
        if num == 0:
            return "0"
        while num > 0:
            binary_string = str(num % 2) + binary_string
            num = num // 2
        return binary_string
    else:
        raise ValueError("Input must be a non-negative integer")
    

