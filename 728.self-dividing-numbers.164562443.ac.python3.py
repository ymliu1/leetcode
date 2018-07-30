class Solution:
    def selfDividingNumbers(self,left, right):
        """
        :Type left: int
        :type right: int
        :rtype: List[int]
        """
        number_list=[]
        final_list=[]
        x=1
        y=1
        j=''
        for i in range(left,right+1):
            count=0
            x=i
            y=i
            number_list=[]
            while x!=0 and y!=0:
                x=y%10
                if x!=0:
                        number_list.append(x)
                else:
                        number_list=[]
                        break
                y=int(y/10)
            
            length=len(number_list)
            if length!=0:
                    for num in number_list:
                            if i%num==0:
                                    count=count+1
                                    if count==length:
                                            final_list.append(i)
        return final_list
                
