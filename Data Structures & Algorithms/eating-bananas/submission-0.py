import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =1
        high = max(piles)
        ans = float('inf')
        while low<= high:
            mid = (low+high)//2
            totalH = sum(math.ceil(p/mid)for p in piles)
            if totalH<= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

        