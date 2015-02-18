from collections import defaultdict
from mathlib import factorize

def count(alist):
    countdict = defaultdict(int)
    for el in alist:
        countdict[el] += 1
    return dict(countdict)

myrange = [el for el in range(1, 21)]

counts = [count(factorize(el)) for el in myrange]

maxcount={}
for acount in counts:
    for key in acount.keys():
        if key not in maxcount or maxcount[key] < acount[key]:
            maxcount[key] = acount[key]

target = 1
for key in maxcount.keys():
    target = target * key**maxcount[key]

print (target)
