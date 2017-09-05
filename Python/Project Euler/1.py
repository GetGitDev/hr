#!/bin/python3

import sys

def check_numbers(number):
    numbers = []
    for i in range(1,number):
        if i % 5 == 0 or i % 3 == 0:
            numbers.append(i)
    return sum(numbers)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    these = check_numbers(n)
    print(these)
