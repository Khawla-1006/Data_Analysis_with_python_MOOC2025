#!/usr/bin/env python3

def triple(param):
    return param*3

def square(param):
    return param**2


def main():
    for i in range(1,10):
        triple_i = triple(i)
        square_i = square(i)
        if square_i <= triple_i:
            print(f"triple({i})=={triple_i} square({i})=={square_i}")
        else:
            break
        


if __name__ == "__main__":
    main()
