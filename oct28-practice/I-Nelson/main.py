import math
import sys

lines = sys.stdin.readlines()
l = lines[0]
N,R,S,W,F,L1,L2 = int(l[0]),float(l[1]),float(l[2]),float(l[3]),float(l[4]),float(l[5]),float(l[6])

races = (float(line) for line in lines[1:])

print(N,R,S,W,F,L1,L2)
print(races)