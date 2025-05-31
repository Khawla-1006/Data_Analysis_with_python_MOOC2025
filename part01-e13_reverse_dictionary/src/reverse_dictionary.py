#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    for old_key,old_value in d.items():
        if len(old_value) == 1 :
            already_there = result.get(old_value[0])
            if already_there :
                already_there.append(old_key)
                result[old_value[0]] = already_there
            else:
                result[old_value[0]]= [old_key]
        else:
            for val in old_value:
                result[val] = [old_key]
    return result
def main():
    #pass
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))



if __name__ == "__main__":
    main()