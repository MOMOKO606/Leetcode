class MyCalendar:

    def __init__(self):
        self.intervals = []
        self.leftpoints = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        k = bisect.bisect_left(self.leftpoints, startTime)
        if k > 0 and startTime < self.intervals[k - 1][1]: return False
        if k < len(self.intervals) and self.intervals[k][0] < endTime: return False
        bisect.insort(self.leftpoints, startTime)
        self.intervals.insert(k, [startTime, endTime])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)