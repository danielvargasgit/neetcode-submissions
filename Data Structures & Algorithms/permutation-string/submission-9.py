class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for right in range(len(s2)):
            left = max(right - len(s1)+ 1,0)
            if sorted(s2[left:right+1]) == sorted(s1):
                return True
        return False
