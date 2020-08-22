class Solution:
    """
    Questions:
    Given a set of distinct integers, nums, return all possible subsets (the power set).
    Note: The solution set must not contain duplicate subsets.
    """

    """
    Solution 1:
    for each new element, create a new uni-set of it and add it to every current subset
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            for each in result[:]:
                result.append(each + [nums[i]])
        return result

    """
    Solution 2: 
    Backtrace
    """