from sys import stdin

def power_p(x, n):
    r = 0
    p = n
    while x//p:
        r += x//p
        p *= n
    return r        

def main():
    readl = stdin.readline    
    for __ in xrange(int(readl())):
        n = int(readl())
        print power_p(n, 5)

if __name__ == "__main__":
    main()
