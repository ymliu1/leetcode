class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=['A', 'a', 'e', 'E', 'I', 'i', 'O', 'o', 'U', 'u']
        sl = list(s) 
        
        index_list=[]
        vowel_list=[]
        for index,value in enumerate(s):
            if value in vowels:
                index_list.append(index)
                vowel_list.append(value)
        vowel_list.reverse()
        length=len(index_list)
        for i in range(length):
            sl[index_list[i]]=vowel_list[i]
        return ''.join(sl)
