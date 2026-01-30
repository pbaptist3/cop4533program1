from match import match
import verifier
import random
from time import time

def time_verify(n):
    i = 0
    in_seq = [n]
    def source():
        nonlocal i
        nonlocal in_seq
        if i == 0:
            i += 1
            return n
        elif i == 1:
            options = [str(i) for i in range(1,n+1)]
            random.shuffle(options)
            shuffled = ' '.join(options)
            in_seq.append(shuffled)
            return shuffled
    
    def sink(out):
        nonlocal in_seq
        in_seq.append(out)

    match(source=source, sink=sink)

    j = 0
    def verify_source():
        nonlocal j
        j += 1
        return in_seq[j-1]
    t1 = time()
    verifier.main(source=verify_source)
    return time() - t1

def benchmark_verify(iters):
    times = []
    for i in range(iters):
        times.append(time_verify(2**i))

    for i, t in enumerate(times):
        print(f"{2**i} {t}")

if __name__=="__main__":
    benchmark_verify(13)
