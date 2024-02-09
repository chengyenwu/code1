# 1221. Split a string in balanced strings 
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "RLRRLLRLRL"
        Llist = ['L']
        Rlist = ['R']
        Lstack = []
        Rstack = []
        k = 0
        for i in s:
            if i in Llist:
                Lstack.append(i)
            else:
                Rstack.append(i)
            if len(Lstack) == len(Rstack):
                k += 1
        return k