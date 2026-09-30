class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in amap:
                amap[key] =[]
            amap[key].append(word)
        return list(amap.values())