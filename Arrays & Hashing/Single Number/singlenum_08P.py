class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            counter = nums.count(num)
            if counter == 1:
               return num    
