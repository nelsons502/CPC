def print_list(nums):
  for i in range(len(nums)):
    print(nums[i], end="")
    print("," if i < len(nums)-1 else "",end="")
  print()
print_list([1,2,3,4,5])
