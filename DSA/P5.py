# Move Zeros

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[k]=0
            k+=1
        return nums


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]