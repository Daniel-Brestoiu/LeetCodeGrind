#Solution for Teemo Attacking problem 495 on LeetCode
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time = 0
        for i in range(0, len(timeSeries) - 1):
            timeDiff = timeSeries[i + 1] - timeSeries[i]
            if (timeDiff < duration):
                time += timeDiff
            else:
                time += duration
        time += duration
        return(time)

                