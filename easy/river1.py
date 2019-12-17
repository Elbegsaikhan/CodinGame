import sys
import math

def nextRiverNumber(riverNumber):
    sum = riverNumber
    while(riverNumber > 0):
        sum += riverNumber %10
        riverNumber //= 10

    return sum
r_1 = int(input())
r_2 = int(input())

while r_1 != r_2:
    if r_1 < r_2:
        r_1 = nextRiverNumber(r_1)
    else :
        r_2 = nextRiverNumber(r_2)


print(r_1)