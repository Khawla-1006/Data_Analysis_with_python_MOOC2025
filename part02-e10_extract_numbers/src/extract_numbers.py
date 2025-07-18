#!/usr/bin/env python3

def extract_numbers(s):
    input_list = s.split()
    result = []
    for item in input_list:
        try:
            x = int(item)
            result.append(x)
        except ValueError:
            try:
                y = float(item)
                result.append(y)
            except ValueError:
                continue
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
