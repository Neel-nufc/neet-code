def backtrack(start):
    if sum(sol) == target:
        res.append(sol[:])
        return 
    
    if sum(sol) > target:
        return 
    
    for i in range(start, len(nums)):
        sol.append(nums[i])
        backtrack(i)
        sol.pop()


target = 7
sol, res = [], []

nums = [2,3,5,7]

backtrack(0)

print(res)