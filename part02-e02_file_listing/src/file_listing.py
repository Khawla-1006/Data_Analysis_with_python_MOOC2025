#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename) as ref:
        for line in ref :
            line = line.strip()
            size_d_h_m = re.findall(r"\b\d+\b",line)
            num = list(map(lambda x: int(x),size_d_h_m[1:]))
            month = re.search(r"\b[A-Z][a-z]{2}\b",line)
            file = re.search(r"\w*(-|\.)*\w*[-]*\w*\.[a-z_]+|\b[A-Z][a-z]{4,}\b|\.\w+\.*\w*|_\w+|\.\w+",line)
            result.append((num[0],month.group(),num[1],num[2],num[3],file.group()))
        return result
def main():
    print(file_listing("listing.txt"))

if __name__ == "__main__":
    main()
