class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxarea = 0
        while i < j:
            height = min(heights[i],heights[j])
            length = j - i
            if (height * length) > maxarea:
                maxarea = height * length
            if heights[i] > heights[j]:
                j = j-1
            else:
                i = i +1
        return maxarea


        