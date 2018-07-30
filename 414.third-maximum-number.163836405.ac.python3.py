class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        new_nums=list(set(nums))
        length=len(new_nums)
        new_nums.sort(reverse=True)
        if length>2:
            return new_nums[2]
        elif length<=2:
            return new_nums[0]
