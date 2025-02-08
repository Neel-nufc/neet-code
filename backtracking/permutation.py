class permutation:
    def __init__(self,nums):
        self.res = []
        self.sol = []
        self.nums = nums 

    def backtrack(self):
        if len(self.sol) == len(self.nums):
            self.res.append(self.sol[:])
        
        for n in self.nums:
            if n not in self.sol:
                self.sol.append(n)
                self.backtrack()
                self.sol.pop()
        

def permute(nums):
    per = permutation(nums)
    per.backtrack()
    return per.res

print(permute([1,2,3]))