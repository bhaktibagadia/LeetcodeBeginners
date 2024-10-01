class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sorteds = tuple(sorted(s))
            if sorteds in dic:
                dic[sorteds].append(s)
            else:
                dic[sorteds] = [s]
        return list(dic.values())            
