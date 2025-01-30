class union_find:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
    
    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return False
        
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

        return True

def find_min_cost(points):
    N = len(points)
    dsu = union_find(N+1)
    edges = []


    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2,y2 = points[j]

            dist = abs(x1-x2) + abs(y1-y2)
            edges.append((dist, i, j))

    edges.sort()
    res = 0

    for dist, i, j in edges:
        if dsu.union(i,j):
            res += dist 
    return res

print(find_min_cost([[0,0],[2,2],[3,10],[5,2],[7,0]]))


