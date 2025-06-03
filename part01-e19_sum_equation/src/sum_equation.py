#!/usr/bin/env python3
from functools import reduce
def sum_equation(L):
    if not L:
        return "0 = 0"
    result = list(map(str,L))
    return " + ".join(result) + f" = {sum(L)}"
def main():
    print(sum_equation([1,2,3,7,5,8,9]))

if __name__ == "__main__":
    main()