class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list=s.split(' ')
        length=len(s_list)
        new_s=''
        for i in range(length):
                s_list[i]=s_list[i][::-1]
                new_s=new_s+s_list[i]+' '
        return new_s.strip()
