from sys import stdin
readl = stdin.readline
 
class  DisjointSet:

    def  __init__(self,  s,  pathop=None):
        self._root  =  set(s)
        self._parent  =  {x: x for x in s}

        if  pathop  ==  'compression':
            self.find  =  self._compression
        elif  pathop  ==  'splitting':
            self.find  =  self._splitting
        elif  pathop  ==  'halving':
            self.find  =  self._halving

    def  _compression(self,  x):
        r  =  x
        while  r  !=  self._parent[r]:
            r  =  self._parent[r]
        while  x  !=  r:
            p  =  self._parent[x]
            self._parent[x]  =  r
            x  =  p
        return x

    def  _splitting(self,  x):
        while  x  !=  self._parent[x]:
            p  =  self._parent[x]
            self._parent[x]  =  self._parent[p]
            x  =  p
        return x

    def  _halving(self,  x):
        while  x  !=  self._parent[x]:
            p  =  self._parent[x]
            self._parent[x]  =  self._parent[p]
            x  =  self._parent[x]
        return x

    def  find(self,  x):
        while  x  !=  self._parent[x]:
            x  =  self._parent[x]
        return x

    def  root_set(self):
        return self._root.copy()

    def  make_set(self,  x):
        if  x  not  in  self._parent:
            self._parent[x]  =  x
            self._root.add(x)
            return True
        else:
            return False

    def  joined(self,  x,  y):
        return (self.find(x)  ==  self.find(y))

    def  join(self,  x,  y):
        rx,  ry  =  self.find(x),  self.find(y)
        if  rx  ==  ry:
            return False
        if  self._parent[rx]  <  self._parent[ry]:
            rx,  ry  =  ry,  rx
        self._parent[ry]  =  rx
        self._root.remove(ry)
        return True

    def  size(self):
        return len(self._root)

    def  __len__(self):
        return len(self._parent)

nv, ne = map(int, readl().split())
ds = DisjointSet(range(nv), pathop='splitting')
for __ in xrange(ne):
    p, q = map(int, readl().split())
    ds.join(p-1, q-1)
 
for __ in xrange(int(readl())):
    p, q = map(int, readl().split())
    pr, qr = ds.find(p-1), ds.find(q-1)
    if pr == qr:
        print("TIE")
    elif pr > qr:
        print(p)
    else:
        print(q)
        
