class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        size = len(intervals)
        pre = newInterval.start
        index = -1
        for x in xrange(0,size):
            a = intervals[x]                        
            if newInterval.start < a.start:
                pre = newInterval.start
                index = x
                break
            elif newInterval.start >= a.start and newInterval.start <= a.end:
                pre = a.start
                index = x
                break
        end = newInterval.end 
        if index != -1:
            delete = []
            for x in xrange(x,size):
                a = intervals[x]
                if newInterval.end > a.end:
                    delete.append(a)
                elif newInterval.end == a.end:
                    delete.append(a)
                    end = a.end
                    break
                elif newInterval.end < a.start:
                    break
                elif newInterval.end == a.start:
                    delete.append(a)
                    end = a.end
                    break
                else:
                    delete.append(a)
                    end = a.end
                    break
            for x in delete:
                if x in intervals:
                    intervals.remove(x)
            flag = True
            for x in xrange(len(intervals)):
                if end < intervals[x].start:
                    intervals.insert(x,Interval(pre,end)) 
                    flag = False  
                    break
            if flag:
                intervals.append(Interval(pre,end))                
        else:
            intervals.append(Interval(pre,end))
        return intervals