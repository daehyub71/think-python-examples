import sys

nums_list = [n * 2 for n in range(100_000)]
nums_gen = (n * 2 for n in range(100_000))

print(sys.getsizeof(nums_list))
print(sys.getsizeof(nums_gen))
print(sum(nums_gen))
print(sum(nums_gen))
