
def combine(n: int, k: int) :
    res = []
    
    def combinations(start, comb):
        if len(comb) == k:
            res.append(comb[:])
            return
        
        for i in range(start,n+1):
            if i not in comb:
                comb.append(i)
                combinations(i,comb)
                comb.pop()
    
    combinations(1,[])
    return res

print(combine(4,3))

        