def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r-l)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        
        else:
            l = mid + 1
    return l

print(binary_search([1, 2, 4, 6, 9, 13, 14, 15],5))