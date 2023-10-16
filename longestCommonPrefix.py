class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""

        letters = []
        index = 0

        for word in strs:
            if letters == []:
                letters.append(word[index])
            else:
                
        

obj = Solution()
obj.longestCommonPrefix(["flower","flow","flight"])