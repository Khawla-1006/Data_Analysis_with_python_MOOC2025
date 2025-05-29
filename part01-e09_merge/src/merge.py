# !/usr/bin/env python3

def merge(L1, L2):
    new_list = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            new_list.append(L1[i])
            i += 1
        else:
            new_list.append(L2[j])
            j += 1
    new_list.extend(L1[i:])
    new_list.extend(L2[j:])
    return new_list

def main():
    a = merge(sorted([1,2,3,4,5,2,4]),sorted([7,8,9,14]))
    print(a)

if __name__ == "__main__":
    main()
