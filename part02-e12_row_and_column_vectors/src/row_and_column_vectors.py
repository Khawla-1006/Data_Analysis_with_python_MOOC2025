#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    res = np.split(a,len(a))
    return res

def get_column_vectors(a):
    r = np.split(a,len(a.T), axis = 1)
    return r

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,2))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
