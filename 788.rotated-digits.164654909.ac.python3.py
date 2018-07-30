class Solution:
    def rotatedDigits(self,N):
        """
        :type N: int
        :rtype: int
        """
        count=0
        length=0
        for i in range(1,N+1):
            x=i
            y=i
            marker=0
            while y!=0:
                x=y%10
                y=int(y/10)
                
                if x in [3,4,7]:
                    marker=0
                    break
                elif x in [2,5,6,9]:
                    marker=1
                                
            if marker==1:
                count=count+1
                
        return count
                    
                    
