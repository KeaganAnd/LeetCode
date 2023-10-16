class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2  != 0:
            return False
        
        for i in range(0, len(s), 2):
            if(not (ord(s[i])-ord(s[i+1]) >= -2 and ord(s[i])-ord(s[i+1]) <= -1)):
                return False
        return True

obj = Solution()
print(obj.isValid("()[]{}"))