import collections
import heapq

def network_delay(times,n,k):
    edges = collections.defaultdict(list)

    for u,v,w in times:
        edges[u].append((v,w))

    min_heap = [(0,k)]
    visited = set()
    time = 0

    while min_heap:
        w1, n1 = heapq.heappop(min_heap)
        if n1 in visited:
            continue

        visited.add(n1)
        time = w1

        for n2, w2 in edges[n1]:
            if n2 not in visited:
                heapq.heappush(min_heap, (w1+w2,n2))
    return time if len(visited) == n else -1
    

# test case 1
print(network_delay([[2,1,1],[2,3,1],[3,4,1]],4,2))