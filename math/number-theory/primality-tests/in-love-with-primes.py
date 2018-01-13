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

def main():
    s = sieve_eratosthenes(10**5)
    for __ in range(int(readl())):
        n = int(readl())
        if n%2:
            print("Arjit")
            continue
        deepa = False    
        for i in range(2, n//2+1):
            if s[i] and s[n-i]:
                deepa = True
                break
        print("Deepa" if deepa else "Arjit")
    
if __name__ == "__main__":
    main()
