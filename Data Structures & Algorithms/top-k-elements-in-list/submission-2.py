class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1
        return sorted(num_map,key = num_map.get, reverse = True)[:k]




        