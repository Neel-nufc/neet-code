from collections import defaultdict
def course(num_course, pre_req):
    pre_map = defaultdict(list)

    for crs, pre in pre_req:
        pre_map[crs].append(pre)
    
    visited = set()

    def dfs(crs):
        if crs in visited:
            return False
        
        if pre_map[crs] == []:
            return True 
        
        visited.add(crs)

        for pre in pre_map[crs]:
            if not dfs(pre):
                return False
        visited.remove(crs)
        pre_map[crs] = []
        return True
    
    for c in range(num_course):
        if not dfs(c):
            return False
    return True


print(course(2, [[0,1]]))
print(course(2,[[0,1],[1,0]]))