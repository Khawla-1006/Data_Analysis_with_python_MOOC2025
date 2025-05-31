#!/usr/bin/env python3

def find_matching(L, pattern):
    c = []
    for i, word in enumerate(L):
        if pattern in word:
            c.append(i)

    return c

def main():
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(result)

if __name__ == "__main__":
    main()
