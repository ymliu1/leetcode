class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        nums.sort()
        min=0
        max=length-1
        if length==1:
            return nums[0]
        while max!=min+1:
            center=int((min+max)/2)
            if center%2==0 and nums[center]==nums[center+1]:
                min=center
            elif center%2==0 and nums[center]<nums[center+1]:
                max=center
            elif center%2!=0 and nums[center]==nums[center+1]:
                max=center
            elif center%2!=0 and nums[center]<nums[center+1]:
                min=center
        if max==min+1:
            if min==0:
                return nums[min]
            else: return nums[max]
        return nums[center]
