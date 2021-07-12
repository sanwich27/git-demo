#!/usr/bin/env python3
def num(n):
    try:
        return int(n)
    except ValueError:
        return float(n)

n = num(input("Enter numerator: "))
d = num(input("Enter denominator: "))
print(n/d)
