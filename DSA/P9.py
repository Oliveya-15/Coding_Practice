# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=x
        s=0
        while x>0:
            r=x%10
            s=s*10+r
            x=x/10
        return s==n
        