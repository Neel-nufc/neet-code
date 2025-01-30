import collections
import heapq

def min_cost_point(points):
    N = len(points)

    min_heap =[(0,0)]

    res = 0 
    visited = set()

    while len(visited) < N:
        dist, point = heapq.heappop(min_heap)

        if point in visited:
            continue 

        visited.add(point)
        res += dist

        x1, y1 = points[point]

        for i in range(N):
            if i not in visited:
                x2, y2 = points[i]

                new_dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(min_heap, (new_dist,i))

    return res

print(min_cost_point([[0,0],[2,2],[3,10],[5,2],[7,0]]))