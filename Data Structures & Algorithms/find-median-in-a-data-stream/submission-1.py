class MedianFinder:

    def __init__(self):
        self.lowerHalf = []
        self.upperHalf = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        # print(num, self.lowerHalf, self.upperHalf)
        if len(self.lowerHalf) > len(self.upperHalf):
            if -self.lowerHalf[0] > num:
                switch = heapq.heappop(self.lowerHalf)
                heapq.heappush(self.lowerHalf, -num)
                heapq.heappush(self.upperHalf, -switch)
            else:
                heapq.heappush(self.upperHalf, num)
        elif len(self.lowerHalf) < len(self.upperHalf):
            if self.upperHalf[0] < num:
                switch = heapq.heappop(self.upperHalf)
                heapq.heappush(self.lowerHalf, -switch)
                heapq.heappush(self.upperHalf, num)
            else:
                heapq.heappush(self.lowerHalf, -num)
        else:
            if not self.upperHalf:
                self.upperHalf.append(num)
            elif self.upperHalf[0] < num:
                switch = heapq.heappop(self.upperHalf)
                heapq.heappush(self.lowerHalf, -switch)
                heapq.heappush(self.upperHalf, num)
            else:
                heapq.heappush(self.lowerHalf, -num)
            

    def findMedian(self) -> float:
        # print(self.lowerHalf, self.upperHalf)
        if self.count % 2 == 0:
            return (-self.lowerHalf[0] + self.upperHalf[0])/2
        else:
            if len(self.lowerHalf) > len(self.upperHalf):
                return -self.lowerHalf[0]
            else:
                return self.upperHalf[0]
        