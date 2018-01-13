from sys import stdin
readl = stdin.readline

def sieve_eratosthenes(n):
    size = n + 1
    sieve = bytearray(b'\x01'*size)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == 1:
            for j in range(i*i, size, i):
                sieve[j] = 0

    return sieve

s = sieve_eratosthenes(10**6)
for __ in range(int(readl())):
    sz, k = map(int, readl().split())
    arr = list(map(int, readl().split()))
    arr = [x for x in arr if s[x]]
    print(sum(arr[k-1::k]))

