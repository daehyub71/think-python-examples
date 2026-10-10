import time
big_list = list(range(2_000_000))
big_set = set(big_list)

start = time.time()
for i in range(50):
    1_999_999 in big_list
print(f"리스트 {time.time() - start:.6f}초")

start = time.time()
for i in range(50):
    1_999_999 in big_set
print(f"집합   {time.time() - start:.6f}초")
