class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl=list(s)
        sl.reverse()
        return ''.join(sl)
