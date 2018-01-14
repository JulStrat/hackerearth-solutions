from sys import stdin, stdout
readl = stdin.readline
write = stdout.write

def sieve_eratosthenes(n):
    size = n + 1
    sieve = bytearray(b'\x01'*size)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == 1:
            for j in range(i*i, size, i):
                sieve[j] = 0
    primes = [i for i in range(2, size) if sieve[i] == 1]                
    return sieve, primes

def main():
    qu = [int(readl()) for __ in range(int(readl()))]
    s, primes = sieve_eratosthenes(10**6)
    cache = {}

    for x in qu:
        if s[x]:
            write("0\n")
            continue
        if x in cache:
            write(str(cache[x]))
            write("\n")
            continue
        for p in primes:
            if not x%p:
                cache[x] = x-p
                write(str(x-p))
                write("\n")
                break

if __name__ == "__main__":
    main()
