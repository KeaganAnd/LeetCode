'''
Generates given row of pascalls triangle
Formula represented as follows:

n!/
k!*(n-k)!

'n' is the row number
'k' is the number in the row
row length will always be one more than n
'''



import math

class Solution:     

    #O(n^2) solution because factorials are nest loops
    def getRow(self, rowIndex: int):
        
        row = []

        n = rowIndex

        for k in range(0, n+1):
           row.append(int((math.factorial(n)/((math.factorial(k))*(math.factorial(n-k))))))

        return(row)
    
    #O(n) because it just goes through the row once without factorials
    def getRow2(self, rowIndex: int):
        row = [1]  # The first element in every row is always 1

        for k in range(1, rowIndex + 1):
            # Calculate the next element using the previous element in the row
            # and the formula C(n, k) = C(n, k-1) * (n - k + 1) / k
            next_element = row[-1] * (rowIndex - k + 1) // k
            row.append(next_element)

        return row
        


obj = Solution()
print(obj.getRow2(3))