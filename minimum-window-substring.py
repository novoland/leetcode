class Solution:
    # @return a string
    def minWindow(self, S, T):
        if not T or not S:
            return ""
        size1,size2 = len(S),len(set(T))
        if size1 < size2:
            return ""
        table = {}
        for x in T:
            table[x] = 1 if x not in table else table[x]+1
        negetive = size2
        path = []
        result = ""
        count = 0
        left = 0
        # print table
        for x in xrange(size1):
            if S[x] in T:
                path.append(x)
                if S[x] in table:
                    table[S[x]] -= 1
                    if table[S[x]] == 0:
                        negetive -= 1
                while negetive == 0:
                    t = path[len(path)-1]-path[left]+1
                    if count==0 or t < count:
                         count = t
                         result = S[path[left]:path[len(path)-1]+1]
                    table[S[path[left]]] += 1
                    if table[S[path[left]]] > 0:
                        negetive += 1
                    left += 1
        return result