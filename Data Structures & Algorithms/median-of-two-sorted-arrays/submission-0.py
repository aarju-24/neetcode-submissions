
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        # Always binary search on the smaller array
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total number of elements
                if (m + n) % 2:
                    return float(max(Aleft, Bleft))

                # Even total number of elements
                return (
                    max(Aleft, Bleft) + min(Aright, Bright)
                ) / 2.0

            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

        return 0.0
