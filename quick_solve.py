N = int(input())
days = []

days_set = set()

for i in range(N):
    line = input().split()
    days.append((int(line[0]),int(line[1])))

for d in days:
    for i in range(d[0],d[1]+1):
        days_set.add(i)

print(len(days_set))