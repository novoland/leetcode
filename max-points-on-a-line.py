class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0
        size = len(points)
        if size == 2:
            return 2
        elif size == 1:
        	return 1
        table = {}        
        points = sorted(points,key=lambda i:i.x)
        count = 2
        for i in xrange(0,size):
            for j in xrange(i+1,size):
                a = points[j].x-points[i].x
                t = float(points[j].y-points[i].y)/a if a else float(100000)
                if t in table:
                    for tmp in table[t]:
                        flag = True
                        if points[i] in tmp or points[j] in tmp:
                            tmp.add(points[i])
                            tmp.add(points[j])
                            flag = False
                            count = len(tmp) if len(tmp) > count else count
                            break
                    if flag:
                          table[t].append(set([points[i],points[j]]))
                else:            
                    table[t] = [set([points[i],points[j]])]    
        return count 