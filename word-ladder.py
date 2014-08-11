class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if start == end:
            return 0 
        length = len(start)
        count = 1
        data = set([start])
        tmp = set()
        char = [chr(c) for c in range(97, 123)]
        while data:
            dest = data.pop()
            for x in xrange(length):
                for y in char:
                    if dest[x] == y:
                        continue
                    else:
                        t = dest[:x]+y+dest[x+1:]
                        # print t
                        if t == end:
                            return count+1
                        if t in dict and t not in data:
                            tmp.add(t)
                            dict.remove(t)
            if not data:
                # print tmp
                data = tmp.copy()
                tmp = set()
                count += 1
        return 0