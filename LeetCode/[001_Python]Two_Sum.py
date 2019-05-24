class Solution1:

    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target
    @param nums an array of integers
    @param target number = nums[index1] + nums[index2]
    @return [index1, index2]
    """

    # Brute Force
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], i+1):
                if b == target - a:
                    return [i, j]
        return ValueError("No two sum solution")
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)



class Solution2:

    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target
    @param nums an array of integers
    @param target number = nums[index1] + nums[index2]
    @return [index1, index2]
    """

    # One-pass Hash Table
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return map[complement], i
            else:
                map[nums[i]] = i
        return ValueError("No two sum solution")
    # Time Complexity: O(n)
    # Space Complexity: O(n)







