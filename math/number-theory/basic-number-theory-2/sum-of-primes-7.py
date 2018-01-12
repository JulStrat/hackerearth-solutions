from sys import stdin
from bisect import bisect_left, bisect_right
readl = stdin.readline

def accumulate(iter):
    r = 0
    for val in iter:
        r += val
        yield r

def Eratosthenes(n):
  ub = n+1
  e = bytearray(b'\x01'*ub)

  for i in xrange(2, int(n**0.5)+1):
    if e[i]:
      for j in xrange(i*i, ub, i):
        e[j] = 0
  return [i for i in xrange(2, ub) if e[i]]

if __name__ == "__main__":
    qu = []
    for __ in xrange(int(readl())):
        l, r = map(int, readl().split())
        qu.append((r, l))
    hi = max(qu)[0]
    primes = Eratosthenes(hi)
    pref_sum = list(accumulate(primes))
    for r, l in qu:
        lo = bisect_left(primes, l)
        hi = bisect_right(primes, r)
        lo_s = 0 if not lo else pref_sum[lo-1]
        hi_s = 0 if not hi else pref_sum[hi-1]
        print(hi_s - lo_s)
