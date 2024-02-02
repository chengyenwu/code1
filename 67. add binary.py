# 67. Add binary
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = []
        carry = 0
        a_index = len(a)-1
        b_index = len(b)-1
        temp = 0
        while a_index >=0 or b_index >=0 or carry:
            if a_index >= 0:
                carry += int(a[a_index])
                a_index-=1
            if b_index >= 0:
                carry += int(b[b_index])
                b_index-=1
            sum.insert(0, str(carry%2))
            carry //= 2
        return "".join(sum)