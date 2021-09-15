def binary_search(nums, target):
    idx = len(nums)//2
    return_idx = idx
    # if len(nums) == 1 and nums[0] == target:
    #     return 0
    if len(nums) == [2]:
        if nums[0] == target:
            return 0
        elif nums[1] == target:
            return 1
        else:
            return -1
    while idx >= 0 and idx < len(nums):
        if len(nums) == 1 and nums[0] != target:
            return -1
        a =nums[idx]
        if target > nums[idx]:
            nums =  nums[idx:]
            idx = len(nums)//2
            return_idx = return_idx + idx
        elif target < nums[idx]:
            nums = nums[:idx]
            idx = len(nums)//2
            return_idx = return_idx - idx
        else:
            return return_idx
    return -1

nums =  [-1,0,3,5,9,12]

target = 0
print(binary_search(nums, target))