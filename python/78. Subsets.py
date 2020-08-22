class Solution:
    """
    Questions:
    Given a set of distinct integers, nums, return all possible subsets (the power set).
    Note: The solution set must not contain duplicate subsets.
    """

    """
    Solution 1: blue force
    for each new element, create a new uni-set of it and add it to every current subset
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            for each in result[:]:
                result.append(each + [nums[i]])
        return result

    """
    Solution 2: Backtrace
    """
    def __init__(self):
        self.result = []
        self.temp = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrace(nums, 0)
        return self.result
    def backtrace(self, nums, start):
        self.result.append(self.temp[:])
        for i in range(start, len(nums)):
            self.temp.append(nums[i])
            self.backtrace(nums, i + 1) # 前面的都已经搜索过了
            self.temp = self.temp[:-1]