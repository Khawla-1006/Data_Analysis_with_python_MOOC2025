#!/usr/bin/env python3

import re

def file_extensions(filename):
    no_extension = []
    ex = []
    my_dict = {}
    with open(filename) as ref:
        files = ref.read().split()
        for file in files :
            if "." not in file :
                no_extension.append(file)
            else:
                ex.append(file)
        #extracting keys for the dict
        keys = []
        for item in ex :
            extension = item[item.rindex(".")+1:]
            if extension not in keys:
                keys.append(extension)
        #filling the dict
        for key in sorted(keys) :
            my_dict[key] = []
        for f in ex :
            for key in keys :
                if key in f :
                    my_dict[key].append(f)
    return (no_extension, my_dict)

def main():
    df = file_extensions("filenames.txt")
    print(f"{len(df[0])} files with no extension")
    for key,value in df[1].items():
        print(f"{key} {len(value)}")
        
if __name__ == "__main__":
    main()
