class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        if len(s) == 1:
            return 1
        s_max = 0
        s_tmp = ""
        for x in s:
            index = s_tmp.find(x)
            if index == -1:
                s_tmp += x
            else:
                s_tmp = s_tmp[index+1:]+x
            if len(s_tmp) > s_max:
                s_max = len(s_tmp)
        return s_max