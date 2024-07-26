class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        current_time = [math.ceil(dist[i]/speed[i]) for i in range(len(dist))]

        current_time.sort()

        output, time = 1,1

        for t in current_time[1:]:
            if t<=time:
                return output
            else:
                output+=1
                time+=1
        return output            