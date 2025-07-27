#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n > 1:
        to_copy = np.eye(n, dtype=int)
        copied = np.concatenate((np.fliplr(to_copy),to_copy), axis=1)
        result = np.concatenate((copied,np.flipud(copied)))
        r = np.delete(result,len(result)-n,axis=1)
        q = np.delete(r,len(result)-n,axis=0)
        return q
    else:
        return np.eye(n,dtype=int)

def main():
    np.random.seed(0)
    print(diamond(2))

if __name__ == "__main__":
    main()
