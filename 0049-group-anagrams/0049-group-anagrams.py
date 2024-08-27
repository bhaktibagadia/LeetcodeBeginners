class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for s in strs:
            sorteds = tuple(sorted(s))
            if sorteds in mpp:
                mpp[sorteds].append(s)
            else:
                mpp[sorteds] = [s]
        return list(mpp.values())        

                    