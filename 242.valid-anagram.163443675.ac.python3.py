class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list=[]
        t_list=[]
        length1=len(s)
        length2=len(t)
        if length1!=length2:
            return False
        if length1==length2:
            for i in range(length1):
                s_list.append(s[i])
                t_list.append(t[i])
        s_list.sort()
        t_list.sort()
        if s_list==t_list:
            return True
        else:
            return False;
