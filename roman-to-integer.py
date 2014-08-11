class Solution:
    # @return an integer
    def romanToInt(self, s):
        if not s:
            return
        result = 0
        t = 0
        for x in xrange(0,len(s)):
            c = s[x]
            if c == 'I':
                if t < 1:
                    result = result+1-2*t
                else:
                    result = result+1
                t = 1
            elif c == 'V':
                if t < 5:
                    result = result+5-2*t  
                else:
                    result = result+5                                  
                t = 5
            elif c == 'X':
                if t < 10:
                    result = result+10-2*t
                else:
                    result = result+10                                    
                t = 10
            elif c == 'L':
                if t < 50:
                    result = result+50-2*t
                else:
                    result = result+50                                    
                t = 50
            elif c == 'C':
                if t < 100:
                    result = result+100-2*t  
                else:
                    result = result+100                                  
                t = 100
            elif c == 'D':
                if t < 500:
                    result = result+500-2*t
                else:
                    result = result+500                                    
                t == 500
            elif c == 'M':
                if t < 1000:
                    result = result+1000-2*t
                else:
                    result = result+1000                                    
                t == 1000

        return result
        