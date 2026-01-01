def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left ] + nums[right]

        if current_sum == target:
            return nums[left], nums[right]
        
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    
    return None

print(two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))