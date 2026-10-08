class Solution:
    def trap(self, height: List[int]) -> int:
    
        n = len(height)
        left = height[0]
        right = height[n-1]
        i = 1
        j = n-2
        rain = 0
        while i <= j:
            
            if right < left:
                if height[j] < right:
            
                    rain += right - height[j]
                else:
                   
                    right = height[j]
                j -= 1
            else:
                if height[i] < left:
                   
                    rain += left - height[i]
                else:
                   
                    left = height[i]
                i += 1
        return rain
