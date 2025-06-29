#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    result = re.findall(r"-*\b\s*\d+\s*\b",s)

    return list(map(lambda x : int(x),result))

def main():
    test = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(test))

if __name__ == "__main__":
    main()
