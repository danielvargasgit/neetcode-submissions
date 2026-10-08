class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        n = len(height)
        left = height[0]
        right = height[n-1]
        i = 1
        j = n-2
        while i =< j:
            if height[i] 
        
        idea:
        from the left we go inward and save the highest block to the left as well as its position. I think that position might be necessary since we need to see what columns to subtract.
        however we can also do 

        let me at first see how I can find most relavent walls.
        '''
        # relevant wall code with 2 pointer saved in arrays
        n = len(height)
        left_arr = []
        for i in range(n):
            if i == 0:
                left_arr.append(height[i])
            else:
                if height[i] > left_arr[i-1]:
                    left_arr.append(height[i])
                else:
                    left_arr.append(left_arr[i-1])
        
        right_arr = []

        j = n-1

        while j >= 0:
            if j == n-1:
                right_arr.append(height[j])
                
            else:
                if height[j] > right_arr[n-2-j]:
                    right_arr.append(height[j])
                else:
                    right_arr.append(right_arr[n-2-j])
            j -= 1

        right_arr_rev = right_arr[::-1]
        rain = 0
        for i in range(n):
            if min(left_arr[i],right_arr_rev[i]) > height[i]:
                rain += min(left_arr[i],right_arr_rev[i]) - height[i]
        return rain
            






        

        
            

            
