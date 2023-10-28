import copy
import math
line= input().split()
N,t = int(line[0]), int(line[1])

def calc_reg_bin(n):
    bin = []
    while n > 0:
        if n%2 == 0:
            bin.insert(0,0)
        else:
            bin.insert(0,1)
        n //= 2
    return bin

outs = []
outs.append(calc_reg_bin(N))
added = True

while added:
    added = False
    add_ons = []
    for bin in outs:
        for i in range(len(bin)-1):
            if bin[i] > 0 and bin[i+1]+2 <= t:
                temp = copy.deepcopy(bin)
                temp[i] -= 1
                temp[i+1] += 2
                add_ons.append(temp)
    for a in add_ons:
        if a not in outs:
            outs.append(a)
            added = True
print(len(outs)%998244353)