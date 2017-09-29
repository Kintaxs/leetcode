class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = ''.join(e for e in s if e.isalnum())

        s = s.lower()

        s_rev = s[::-1]

        return (s == s_rev)
