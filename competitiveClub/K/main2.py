import sys

lines = sys.stdin.readlines()

half1 = lines[:len(lines)//2]
half2 = lines[len(lines)//2+1:]

icpc = {}
outsrc = {}

for l in half1:
    icpc[l.split()[0]+" "+l.split()[1]] = l.split()[2]
for l in half2:
    outsrc[l.split()[0]+" "+l.split()[1]] = l.split()[2]


def remove_repeats(dict1,dict2):
    repeats = set()
    for name in dict1:
        if name.lower() in dict2:
            repeats.add(name)
    for name in repeats:
        del dict1[name]
        del dict2[name.lower()]


remove_repeats(icpc,outsrc)
remove_repeats(outsrc,icpc)


def remove_repeats_vals(dict1,dict2):
    repeats = set()
    for name in dict1:
        if dict1[name].lower() in dict2.values():
            repeats.add(dict1[name])
    for val in repeats:
        for name in dict1:
            if dict1[name] == val:
                del dict1[name]
                break
        for name in dict2:
            if dict2[name] == val.lower():
                del dict2[name]
                break

remove_repeats_vals(icpc,outsrc)
remove_repeats_vals(outsrc,icpc)

if len(icpc) == 0 or len(outsrc) == 0:
    print("No mismatches")
for name in icpc:
    print("I " + icpc[name] + " " + name.split()[1] + " " + name.split()[0])
for name in outsrc:
    print("O " + outsrc[name] + " " + name.split()[1] + " " + name.split()[0])