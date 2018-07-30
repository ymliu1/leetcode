class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        length=len(nums)
        count_list=[]
        miss_number=0
        twice_number=0
        for i in range(length):
            count_list.append(0)
        for i in range(length):
            count_list[nums[i]-1]=count_list[nums[i]-1]+1
        for i in range(length):
            if count_list[i]==0:
                miss_number=i+1
            elif count_list[i]==2:
                twice_number=i+1
            if miss_number!=0 and twice_number!=0:
                break
        return (twice_number,miss_number)
        
