class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq ={}
        for x in nums:
            freq[x]= freq.get(x,0)+1
        for x in nums:
            if freq[x] >=2:
                return True
        return False