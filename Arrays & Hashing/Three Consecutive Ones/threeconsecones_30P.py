class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = []
        for num in arr:
          if len(odds) == 3:
            return True
          elif num % 2 != 0:
            odds.append(num)
            continue
          else:
            odds.clear()
        if len(odds) == 3:
            return True
        else:
            return False
