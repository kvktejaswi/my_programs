## program to validate prime number with sqrt(N) time complexity
from math import *
n = int(input("Enter a number: "))
if n<=1:
    is_prime = False
else:
    is_prime = True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            is_prime = False
            break

if is_prime:
    print(f"The given numbert: {n} is PRIME")
else:
    print(f"The given numbert: {n} is NOT PRIME")