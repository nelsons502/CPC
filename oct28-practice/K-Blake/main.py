import math
import sys

all_rows = sys.stdin.readlines()
all_rows = [l for l in all_rows]

all_rows = [l.split() for l in all_rows]

if [] in all_rows:
    all_rows.remove([])

rows = {}

for l in all_rows:
    rows[l[0]+" "+l[1]] = l[2]

names = {}
emails = {}
answer = {}

print('all rows: ', rows)

for row in all_rows:
    full_name = (row[0] + " " + row[1])
    email = row[2]

    if (full_name.lower() not in names):
        names[full_name] = 1
    else:
        names[full_name] += 1

    if (email not in emails):
        emails[email] = 1
    else:
        emails[email] += 1

print(names)
print(emails)

for key in names:
    if (names[key] > 1):
        for row_key in rows:
            if row_key.lower() == key:
                del rows[row_key]
                break

for key in emails:
    if (emails[key] > 1):
        for r in rows:
            if rows[r].lower() == key:
                del rows[r]
                break

n = len(rows)
index = 0

if (n == 0):
    print("No mismatches")

for row in rows:

    if (index < (n / 2)):
        print("I " + rows[row] + " " + row.split()[1] + " " + row.split()[0])
    else:
        print("O " + rows[row] + " " + row.split()[1] + " " + row.split()[0])

    index += 1