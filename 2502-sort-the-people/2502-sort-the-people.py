class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            pivot=i
            for j in range(i+1, len(heights)):
                if heights[j]>heights[pivot]:
                    pivot=j
            names[i], names[pivot] = names[pivot], names[i]
            heights[i], heights[pivot] = heights[pivot], heights[i]
        return names            