class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        index_list=[]
        if target%2==0:
            new_target=int(target/2)
            if nums.count(new_target)==2:
                for i in range(length):
                    if nums[i]==new_target:
                        index_list.append(i)
                index1=index_list[0]
                index2=index_list[1]
                return [index1,index2]
        
        
        new_numbers=list(set(nums))
        length2=len(new_numbers)
        for i in range(length2):
            for j in range(i+1,length2):
                    
                if new_numbers[i]+new_numbers[j]==target and new_numbers[i]!=new_numbers[j]:
                    index1=nums.index(new_numbers[i])
                    index2=nums.index(new_numbers[j])
                    return [index1,index2]
                    
