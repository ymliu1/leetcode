class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_start=0
        sub_end=0
        sort_nums=sorted(nums)
        
        length=len(nums)
        if sort_nums==nums:
            return 0
        for i in range(length):
            if nums[i]!=sort_nums[i]:
                sub_start=i
                
                break
        for i in range(length-1,0,-1):
            if nums[i]!=sort_nums[i]:
                sub_end=i
                
                break
        return (sub_end-sub_start+1)
