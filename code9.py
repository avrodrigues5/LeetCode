class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if len(str(x)) == 1:
            return True
        if "-" in str(x):
            """a=str(x)[1::]
            y=a[::-1]
            z="-"+y
            """
            return False
        else:
            z = str(x)[::-1]
        if x == int(z):
            return True
        else:
            return False


