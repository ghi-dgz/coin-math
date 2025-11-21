import random
import math

def count_attempts(n: int):
    h = 0
    a = 0
    while h < n:
        if random.getrandbits(1):
            h += 1
        else:
            h = 0
        a += 1
    return a

def multitry(func, n, count: int):
    outputs = [func(n) for _ in range(count)]
    return sum(outputs) / count

n = 5
tries = max(16, int(80/n)) # help i dont 
result = multitry(count_attempts, n, 2**tries)
print(f"To get {n} heads in a row:")
print(f"Expected number of flips: {(2 ** (n + 1) - 2)}")
print(f"Average flips in 2^{tries} tries: {result:.2f}")