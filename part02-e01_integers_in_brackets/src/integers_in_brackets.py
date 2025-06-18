#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    result = re.findall(r"[-\d]+",s)
    #FIX THIS SHIT
    return result

def main():
    test = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(test))

if __name__ == "__main__":
    main()
