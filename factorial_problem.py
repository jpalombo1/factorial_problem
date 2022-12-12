import math
import time

nums = [i for i in range(100)]

t0 = time.time()
for a in nums:
    for b in nums:
        for c in nums:
            concat = a * 100 + b * 10 + c
            fact = math.factorial(a) + math.factorial(b) + math.factorial(c)
            if concat == fact:
                print(("{0}{1}{2} = {0}!+{1}!+{2}!").format(a, b, c))

total_time = time.time() - t0
print("Time Loops: {0} ms".format(round((total_time * 1000), 3)))

t1 = time.time()
concat_list = [a * 100 + b * 10 + c for a in nums for b in nums for c in nums]
fact_list = [
    math.factorial(a) + math.factorial(b) + math.factorial(c)
    for a in nums
    for b in nums
    for c in nums
]

for n, entry in enumerate(concat_list):
    if fact_list[n] == concat_list[n]:
        abc = str(concat_list[n])
        print(("{0}{1}{2} = {0}!+{1}!+{2}!").format(abc[0], abc[1], abc[2]))
total_time = time.time() - t1
print("Time Lists: {0} ms".format(round((total_time * 1000), 3)))
