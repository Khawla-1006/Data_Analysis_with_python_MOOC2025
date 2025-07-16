#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename) as ref:
        lines = ref.read()
        l = lines.splitlines()
        w = lines.split()

    return (len(l), len(w), len(lines))

def main():
    for param in sys.argv[1:]:
        file = file_count(param)
        print(f"{file[0]}\t{file[1]}\t{file[2]}\t{param}")

if __name__ == "__main__":
    main()
