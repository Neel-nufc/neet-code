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

        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
def swim(grid):
    rows, cols = len(grid), len(grid[0])
    dsu = union_find(rows*cols)

    edges = [(grid[r][c],r,c) for r in range(rows) for c in range(cols)]

    edges.sort()

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for dist, r, c in edges:
        for dr, dc in directions:
            nr, nc = r +dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] <= dist:
                dsu.union(nr*cols+nc, r*rows+c)
        if dsu.is_connected(0,rows*cols-1):
            return dist
        
grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]]

print(swim(grid))