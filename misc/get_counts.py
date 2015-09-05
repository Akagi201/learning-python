#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    return counts

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=3):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

from collections import Counter

if __name__ == "__main__":
    a = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]
    b = get_counts(a)
    #b = get_counts2(a)
    print(b)
    c = top_counts(b)
    print(c)

    counts = Counter(a)
    d = counts.most_common(3)
    print(d)

