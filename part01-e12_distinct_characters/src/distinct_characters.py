#!/usr/bin/env python3

def distinct_characters(L):
    result = {}
    for item in L :
        result[item] = len(set(item))
    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
