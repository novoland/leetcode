class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if not words or not L:
            return [""]
        result = []
        index,size=0,len(words)
        path,length = [],0
        while index < size:
            if path:
                path.append(' ')  
                length += 1  
            path.append(words[index])   
            length += len(words[index])
            if length == L:
                result.append("".join(path))
                path,length = [],0
                index += 1
            elif length > L:
                length -= len(path.pop())
                length -= len(path.pop())
                sizepath = len(path) 
                last = L-length
                while last:
                    if sizepath==1:
                        path[0] += " "
                        last -= 1
                        continue
                    for x in xrange(0,sizepath):
                        if path[x].find(" ")==0:
                            path[x] += " "
                            last -= 1
                            if last == 0:
                                break
                    else:
                        continue
                    break
                result.append("".join(path))
                path,length = [],0
            else:
                if index == size-1:
                    str = "".join(path)+" "*(L-length)
                    result.append(str)
                index += 1
        return result