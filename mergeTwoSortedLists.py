# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        newList = []

        newList = list1 + list2
        newList.sort()
        return(newList)
        
obj = Solution()

print(obj.mergeTwoLists([1,2,4], [1,3,4]))