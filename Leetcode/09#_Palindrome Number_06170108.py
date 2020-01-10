class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        int_r = x
        str_r = str(int_r)
        if str_r == str_r[::-1]:
            return True
        else:
            return False
