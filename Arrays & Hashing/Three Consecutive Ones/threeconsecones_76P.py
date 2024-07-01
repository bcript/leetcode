class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_counts = 0
        for num in arr:
          if odd_counts == 3:
            return True
          elif num % 2 != 0:
            odd_counts += 1
          else:
            odd_counts -= odd_counts
        if odd_counts == 3:
          return True
        return False
