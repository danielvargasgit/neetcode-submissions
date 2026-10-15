from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        need to figure out how to initialize shortest.
        if condition is never met return ''
        if condition is met once, set shortest
        goal is to move left closest to right so we need to use a while condition

        I can re purpose the last questions counts
        and try to maintain counts == 1

        '''

        # setting target hash table
        t_hash = Counter(t)
        need = len(t_hash)
        have = 0
        window = {}

        best_len = float('inf')
        best_start = 0
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in t_hash and window[c] == t_hash[c]:
                have += 1

            while have == need:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_c = s[left]
                window[left_c] -= 1
                if left_c in t_hash and window[left_c] < t_hash[left_c]:
                    have -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]
                
               

                




        
        