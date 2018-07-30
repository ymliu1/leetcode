class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        number_list=[2,3,5]
        marker=0
        if num<=0:
            marker=0
        if num==1:
            marker=1
        if num>1:
            for i in number_list:
                while num%i==0:
                    num=num/i
                    if num==1:
                        marker=1
                        break
        if marker==1:
            return True
        else:
            return False
                
            
            
