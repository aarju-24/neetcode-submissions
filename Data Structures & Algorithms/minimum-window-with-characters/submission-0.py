class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)

        if n1 < n2:
            return ""

        freqs = {}
        freqt = {}

        # 1. Build the required frequency dictionary for t
        for ch in t:
            freqt[ch] = freqt.get(ch, 0) + 1

        left = 0
        have = 0
        need = len(freqt)

        min_length = float("inf")
        start_index = 0

        # 2. Expand the window using right
        for right in range(len(s)):
            ch = s[right]
            freqs[ch] = freqs.get(ch, 0) + 1

            # 3. Check whether a required character is satisfied
            if ch in freqt and freqs[ch] == freqt[ch]:
                have += 1

            # 4. Shrink the window while it is valid
            while have == need:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    start_index = left

                left_char = s[left]

                if left_char in freqt and freqs[left_char] == freqt[left_char]:
                    have -= 1

                freqs[left_char] -= 1
                left += 1

        # 5. Return the shortest valid substring
        if min_length == float("inf"):
            return ""

        return s[start_index:start_index + min_length]
