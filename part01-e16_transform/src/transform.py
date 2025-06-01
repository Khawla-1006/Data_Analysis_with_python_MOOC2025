#!/usr/bin/env python3

def transform(s1, s2):
    result = [a*b for (a,b) in zip(map(int,s1.split()),map(int,s2.split()))]
    return result
def main():
    print(transform("1 2 8","-1 -1 -1"))

if __name__ == "__main__":
    main()
