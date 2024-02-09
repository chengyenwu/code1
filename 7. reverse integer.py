# 7. Reverse integer
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            sign = '+'
        else:
            sign = '-'
        val = str(abs(x))
        reverse_val = val[::-1]
        reverse_num = int(sign + reverse_val)

        if reverse_num >= 2 ** 31 -1 or reverse_num <= -2 ** 31:
            return 0
        else:
            return reverse_num