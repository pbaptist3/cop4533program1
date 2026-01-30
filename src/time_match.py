from match import match
import random
from time import time

def time_match(n):
    i = 0
    def source():
        nonlocal i
        if i == 0:
            i += 1
            return n
        elif i == 1:
            options = [str(i) for i in range(1,n+1)]
            random.shuffle(options)
            return ' '.join(options)
    
    t1 = time()
    match(source=source)
    return time() - t1

def benchmark_match(iters):
    times = []
    for i in range(iters):
        times.append(time_match(2**i))

    for i, t in enumerate(times):
        print(f"{2**i} {t}")

if __name__=="__main__":
    benchmark_match(13)
