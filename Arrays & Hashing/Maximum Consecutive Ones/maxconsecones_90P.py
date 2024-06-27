class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = []
        consec = []
        nums.append(0)
        for i in range(len(nums)):
          if nums[i] == 0:
            consecutive.append(i)

        for i in range(len(consecutive)):
          if i == 0:
            consec.append(consecutive[i])
          else:
            consec.append(consecutive[i]-consecutive[i-1] - 1)
        return max(consec)
