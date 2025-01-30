import heapq

def min_effort_path(heights):
    rows, cols = len(heights), len(heights[0])
    visited = set()
    
    directions = [(-1,0),(1,0),(0,1),(0,-1)]

    min_heap =[(0,0,0)]

    while min_heap:
        diff, r, c = heapq.heappop(min_heap)

        if (r,c) in visited:
            continue 

        if r == rows - 1 and c == cols - 1:
            return diff
        
        visited.add((r,c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr,nc) in visited:
                continue

            new_diff = max(diff, abs(heights[r][c] -  heights[nr][nc]))
            heapq.heappush(min_heap, (new_diff,nr,nc))

print(min_effort_path([[1,2,2],[3,8,2],[5,3,5]]))