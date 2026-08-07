class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i in range(len(s)):
            hm[s[i]] = i
        currMax = 0
        prev = 0
        partitions = []
        for i, c in enumerate(s):
            currMax = max(currMax, hm[c])
            if i == currMax:
                partitions.append(i - prev + 1)
                prev = i + 1
        return partitions