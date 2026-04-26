from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time taken: 20 min

        Overall complexity: O(n)
        """
        freq = Counter(s1)
        l, r = 0, 0
        while r < len(s2): # O(n), worst case there's no answer and l and r both have n iterations
            if not any(freq.values()): # O(26) = O(1)
                return True
            if s2[r] not in freq:
                while l < r:
                    freq[s2[l]] += 1
                    l += 1
                r += 1
                l = r
                continue
            freq[s2[r]] -= 1
            if freq[s2[r]] < 0:
                # Including current r will drop it's count to negative
                # (too many of s2[r] in the current window)
                # Move up l until freq[s2[r]]= 1
                # (when it finds its fist s2[r] to remove)
                while l < r and freq[s2[r]] < 0:
                    freq[s2[l]] += 1
                    l += 1
            r += 1
        return not any(freq.values())
