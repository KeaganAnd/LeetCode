'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.'''

import time

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """ indexOne = 0
        indexTwo = 1



        while (indexOne < (len(nums)-1)) and (indexTwo <= (len(nums)-1)):
            #print(indexOne, indexTwo)
            #print(nums[indexOne]+nums[indexTwo])
            if nums[indexOne]+nums[indexTwo] == target and indexTwo != indexOne:
                return([indexOne, indexTwo])

            else:
                if indexTwo < (len(nums)-1):
                    indexTwo += 1
                                    
                else:
                    indexTwo = 0
                    indexOne +=1 """
        
        self.num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in self.num_dict:
                return [self.num_dict[complement], i]
            self.num_dict[num] = i
        
        return None
obj = Solution()

list = [1,5,7,2,87,3,23,56]

print(obj.twoSum(list, 26))
print(obj.num_dict)