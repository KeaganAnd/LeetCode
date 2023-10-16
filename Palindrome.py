'''Given an integer x, return true if x is a 
palindrome
, and false otherwise.'''

class Solution(object):
    def isPalindrome(self, x):
        
        digits = []

        for char in str(x):
            digits.append(char)

        digitsReversed = digits.copy()
        digitsReversed.reverse()

        if digits == digitsReversed:
            return True
        else:
            return False
        
obj = Solution()



print(obj.isPalindrome(151))
