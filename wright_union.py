#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 00:57:17 2024

@author: neeleshkumar
"""

class WeightUnion:
    def __init__(self,size):
        self.size = size 
        self.id = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i 
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        id_p = self.root(p)
        id_q = self.root(q)
        
        if id_p == id_q:
            return 
        elif self.rank[id_p] > self.rank[id_q]:
            self.id[id_q] = id_p
            self.rank[id_q] += self.rank[id_p]
        else:
            self.id[id_p] = id_q
            self.rank[id_p] + self.rank[id_q]
            
import time 

start_time = time.time()
            
uf = WeightUnion(10)
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)

print(uf.connected(1, 3))  # True (1, 2, 3 are connected).
print(uf.connected(1, 4))  # False (1 and 4 are not connected).

uf.union(3, 4)
print(uf.connected(1, 5))

end_time = time.time()

print(end_time -  start_time)
        
        