#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    h= triangle.hypotenuse(3,5)
    print(h)
    a = triangle.area(4,2)
    print(a)


if __name__ == "__main__":
    main()
