class Solution:
    def rotate(self,nums, k):
        """
        :Type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        
        if k>=length:
            k=k%length
        if k==0 or length==1:
            return None
        if length%k==0:
            for i in range(k):
                tmp=nums[length-1-i]
                for j in range(length-1-i,-1,-k):
                    
                    if j-k>=0:
                        nums[j]=nums[j-k]
                    elif j-k<0:
                        nums[j]=tmp
            
        elif length%k!=0:
            tmp=nums[length-1]
            i=length-1
            while True:
                if i-k>=0:
                    nums[i]=nums[i-k]
                    i=i-k
                    
                elif i-k<0:
                    nums[i]=nums[i-k]
                    i=i+length-k
                    if i==length-1:
                        nums[k-1]=tmp
                        break
                        
