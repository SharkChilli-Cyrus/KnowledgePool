"""
Question:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

# Answer 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = []
        
        count = 0
        for _ in range(len(nums)):
            temp_nums = nums.copy()
            
            firstNum = temp_nums.pop(count)
            secondNum = target - firstNum
            
            if secondNum in temp_nums:
                firstIndex_list = [index for index, value in enumerate(nums) if value == firstNum]
                secondIndex_list = [index for index, value in enumerate(nums) if value == secondNum]
                if firstNum == secondNum:
                    results.extend([firstIndex_list[0], secondIndex_list[1]])
                else:
                    results.extend([firstIndex_list[0], secondIndex_list[0]])
                    
                break
            else:
                count += 1
                
        return results

# Answer 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            result = target - num
            
            if result in seen:
                return [seen[result], index]
            else:
                seen[num] = index