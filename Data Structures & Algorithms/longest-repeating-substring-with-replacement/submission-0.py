class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        freq ={}
        max_length =0
        for right in range(len(s)):
            freq[s[right]]= freq.get(s[right],0)+1
            while (right-left+1)-max(freq.values())>k:
                freq[s[left]]-=1
                left+=1
                
            max_length = max(max_length,right-left+1)
        return max_length