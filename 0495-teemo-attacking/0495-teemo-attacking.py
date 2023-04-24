class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0: return 0
        totalTime = 0
        for i in range(0, len(timeSeries) - 1):
            totalTime += min(timeSeries[i + 1] - timeSeries[i], duration)
        return totalTime + duration