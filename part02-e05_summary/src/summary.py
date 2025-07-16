#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    wx = []
    with open(filename) as ref:
        f = ref.read().split()
        for item in f :
            try:
                i = float(item)
                wx.append(i)
            except:
                pass
    s = sum(wx)
    av = sum(wx)/len(wx)
    std = 0
    for i in wx:
        std += ((i - av)**2)/(len(wx)-1)
    std_av= sqrt(std)
    return (s,av,std_av)

def main():
    for param in sys.argv[1:]:
        t = summary(param)
        print(f"File: {sys.argv[0]} Sum: {t[0]:.6f} Average: {t[1]:.6f} Stddev: {t[2]:.6f}")

if __name__ == "__main__":
    main()
