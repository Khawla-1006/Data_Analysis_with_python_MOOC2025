def detect_ranges(L):
    s = sorted(L)
    my_list = []
    i = 0
    while i < len(s):
        item = s[i]
        if item+1 not in s:
            my_list.append(item)
        else:
            start = item
            end = item
            s.remove(item)
            while end+1 in L:
                end = end+1
                s.remove(end)
            t = (start, end+1)
            my_list.append(t)
            i-=1
        i+=1
    return my_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
