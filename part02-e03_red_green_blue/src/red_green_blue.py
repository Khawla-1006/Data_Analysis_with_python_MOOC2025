#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename) as ref:
        colors = ref.readlines()
        colors = colors[1:]
    for color in colors:
        nc = color.strip()
        k = re.sub(r"[^\w]+","\t",nc,count=3)
        result.append(k)
    return result


def main():
    print(red_green_blue("rgb.txt"))

if __name__ == "__main__":
    main()
