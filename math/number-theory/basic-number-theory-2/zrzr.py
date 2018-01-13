from sys import stdin
readl = stdin.readline

def power_p(x, n):
    r = 0
    p = n
    while x//p:
        r += x//p
        p *= n
    return r        

def main():
    for __ in range(int(readl())):
        n = int(readl())
        print (min(power_p(n, 2), power_p(n, 5)))

if __name__ == "__main__":
    main()
