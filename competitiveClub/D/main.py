import sys


str = sys.stdin.readlines()
answers = []
strList= [l.strip() for l in str]


for str in strList:
    seen = set()
    seqSoFar = set()
    sequence = ""
    letterSet = set()
    count = 0
    for c in str: 
        letterSet.add(c)
    if len(letterSet) == len(str):
        answers.append(0)
        continue
    if len(letterSet) == 1 and len(str) > 1:
        answers.append(1)
        continue
    for j in range(len(str)): # outer loop
        seen.add(str[j])
        sequence = str[j]
        for i in range(j+1,len(str)):
            if str[i] == str[j]:
                seen.clear()
                break
            else:
                seen.add(str[i])
                sequence = sequence + str[i]
            if len(seen) == len(letterSet):
                if sequence not in seqSoFar:
                    seqSoFar.add(sequence)
                    count +=1
                    seen.clear()
                    break
                else:
                    seen.clear()
                    break
    answers.append(count)

for answer in answers:
    print(answer)



        

