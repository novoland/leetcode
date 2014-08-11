class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        def getpath(path,word):
            if len(preMap[word])==0:
                path.append(word)
                curpath = path[:]
                curpath.reverse()                
                paths.append(curpath)
                path.pop()
                return
            path.append(word)
            for x in preMap[word]:
                getpath(path,x)
            path.pop()
                    
        if start == end:
            return [[start]] 
        length = len(start)
        paths = []
        preMap = {}
        for x in dict:
            preMap[x] = []
        stack=[set(),set()];cur=0;pre=1
        stack[cur].add(start)
        while True:
            cur,pre = pre,cur
            for x in stack[pre]:
                dict.remove(x)
            stack[cur].clear()
            for word in stack[pre]:
                for x in xrange(length):
                    part1 = word[:x];part2 = word[x+1:]
                    for y in 'abcdefghijklmnopqrstuvwxyz':
                        nextword = part1 + y + part2
                        if nextword in dict:
                            stack[cur].add(nextword)
                            preMap[nextword].append(word)
            if len(stack[cur])==0:
                return paths
            if end in stack[cur]:
                break

        getpath([],end)
        return paths