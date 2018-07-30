class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        new_list=list(set(chars))
        new_list.sort()
        count_list=[]
        x_list=[]
        length=len(new_list)
        for i in range(length):
            n=chars.count(new_list[i])
            if n!=1:
                count_list.append(new_list[i])
                if n<=9:
                         count_list.append(str(n))
                elif  n>=10:
                        while n!=0:
                                x=str(n%10)
                                n=int(n/10)
                                x_list.append(x)
                                length3=len(x_list)
                        x_list.reverse()
                        for j in range(length3):
                                count_list.append(x_list[j])
                        x_list=[]
            if n==1:
                count_list.append(new_list[i])
        
        return count_list
