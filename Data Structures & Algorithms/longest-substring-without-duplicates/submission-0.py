class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen ={}
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char]>=left:
                left = seen[char]+1
            seen[char]= right
            window_length = right-left+1
            max_length = max(max_length,window_length)
        return max_length