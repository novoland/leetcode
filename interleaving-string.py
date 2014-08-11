class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if not s3:
            return False
        result = False
        table=set()
        cur = 0
        if s1[0] == s3[0]:
            table.add((1,0))
            cur = 1
        if s2[0] == s3[0]:
            table.add((0,1))
            cur = 1
        while table :
            # print table
            new = set()
            for x in table:
                if x[0] < len(s1) and cur < len(s3) and s1[x[0]] == s3[cur]:
                    new.add((x[0]+1,x[1]))
                if x[1] < len(s2) and cur < len(s3) and s2[x[1]] == s3[cur]:
                    new.add((x[0],x[1]+1))     
            cur += 1
            table = new
            if (len(s1),len(s2)) in table:
                return True if cur == len(s3) else False
        return result