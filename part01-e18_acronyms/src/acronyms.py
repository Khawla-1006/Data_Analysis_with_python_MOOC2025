#!/usr/bin/env python3
from string import punctuation

def acronyms(s):
    x = list(map(lambda word: word.strip(punctuation),s.split()))
    return list(filter(lambda d : d.isupper() and d.isalnum(),x))
def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))

if __name__ == "__main__":
    main()
