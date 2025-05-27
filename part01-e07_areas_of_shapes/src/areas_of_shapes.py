#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    valid_shapes = ["triangle","rectangle","circle"]
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        if shape not in valid_shapes:
            print("Unknown shape!")
        if shape == valid_shapes[0]:
            base = int(input("Give base of the triangle: "))
            t_height = int(input("Give height of the triangle: "))
            print(f"The area is {base*t_height*0.5}")
        if shape == valid_shapes[1]:
            width = int(input("Give width of the rectangle: "))
            r_height = int(input("Give height of the rectangle: "))
            print(f"The area is {width*r_height}")
        if shape == valid_shapes[2]:
            radius = int(input(f"Give radius of the circle: "))
            print(f"The area is {radius**2 * math.pi}")
if __name__ == "__main__":
    main()
