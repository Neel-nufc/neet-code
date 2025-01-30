from collections import defaultdict

def course(num_course, pre_req):
    pre_map = defaultdict(list)

    for crs, pre in pre_req:
        pre_map[crs].append(pre)
    
    cycle = set()
    visited = set()
    output =[]

    def dfs(crs):
        if crs in cycle:
            return False
        
        if crs in visited:
            return True 
        
        cycle.add(crs)
        
        for pre in pre_map[crs]:
            if not dfs(pre):
                return False
            
        
        cycle.remove(crs)
        visited.add(crs)
        output.append(crs)
        
        return True 
    
    for i in range(num_course):
        if not dfs(i):
            return []
        
    return output

print(course(2, [[0,1]]))
print(course(2,[[0,1],[1,0]]))