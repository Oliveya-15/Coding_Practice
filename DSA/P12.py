# Find all Numbers disappeared in an array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                n.append(i)
        return n

"""
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""
