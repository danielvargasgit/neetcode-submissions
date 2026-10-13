class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = {}
        left = 0
        max_freq = 0
        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]] += 1
            else:
                counts[s[right]] = 1
            max_freq = max(max_freq, counts[s[right]])
            while (right - left +1 - max_freq) > k:
                max_freq = max(max_freq, counts[s[right]])
                counts[s[left]] -= 1
                left += 1
            longest = max(longest, right-left+1)

        return longest

