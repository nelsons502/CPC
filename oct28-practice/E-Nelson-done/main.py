import math
import sys

nums = sys.stdin.readlines()

nums = [(int(l.split()[0]),float(l.split()[1])) for l in nums]

for n in nums:
    r = n[0]
    s = n[1]
    v = math.sqrt((r*(s+.16))/.067)
    v = int(v+0.5)
    print(v)