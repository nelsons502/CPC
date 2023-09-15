N = int(input())

num_spots = 2

for i in range(0, N):
    num_spots += 2**i

print(num_spots**2)