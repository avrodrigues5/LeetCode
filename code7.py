class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = (int(str(x)[::-1]) if x > 0 else int(str(x * -1)[::-1]) * -1)
        return 0 if abs(num) > 2 ** 31 - 1 else num
