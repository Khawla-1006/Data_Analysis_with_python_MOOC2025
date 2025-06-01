#!/usr/bin/env python3

def main():
    result = [(i,j) for i in range(1,7) for j in range(1,7) if i + j == 5]
    for r in result:
        print(r)
if __name__ == "__main__":
    main()
