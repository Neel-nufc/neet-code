def twoSum(nums, target):
    seen = {}
    for n in range(len(nums)):
        diff = target - nums[n]
        if diff in seen:
            return list([n, seen[diff]])
        seen[nums[n]] = n


print(twoSum([2,7,11,15],9))