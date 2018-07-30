class Solution:
    def shortestToChar(self,S, C):
        """
        :Type S: str
        :type C: str
        :rtype: List[int]
        """
        length=len(S)
        new_list=[]
        c_list=[]
        for i in range(length):
              new_list.append(1)
        
        for i in range(length):

            if S[i]==C:
                c_list.append(i)
                new_list[i]=0
                for j in range(i-1,-1,-1):
                    if new_list[j]==0:
                        break
                    else:
                        new_list[j]=i-j
                       
                    if  new_list[j-1]==0 :
                        break
        length2=len(c_list)
    
        last_letter=c_list[-1]
        
        for n in range(last_letter+1,length):
            new_list[n]=n-c_list[-1]
        for n in range(length2-1):
                if c_list[n]+1!=c_list[n+1]:
                        for j in range(c_list[n]+1,c_list[n+1]):
                                new_list[j]=j-c_list[n]
                                if new_list[j]>=new_list[j+1]:
                                        break
                

        return new_list
