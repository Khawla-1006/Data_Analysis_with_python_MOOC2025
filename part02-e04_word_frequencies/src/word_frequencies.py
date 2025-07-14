#!/usr/bin/env python3

def word_frequencies(filename):
    result = {}
    ref_list = []
    with open(filename) as ref :
        lines = ref.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            clean_word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
            ref_list.append(clean_word)
    for word in ref_list:
        c = ref_list.count(word)
        result[word] = c
    return result


def main():
    print(word_frequencies("alice.txt"))

if __name__ == "__main__":
    main()
