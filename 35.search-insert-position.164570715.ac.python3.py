class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        for index,value in enumerate(nums):
            
            
            if target==value:
                return index
            elif target<nums[0]:
                return 0
            elif target>nums[length-1]:
                return length
            elif target>value and target<nums[index+1]:
                    return index+1
