# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def firstBadVersion(left, right):
            if left == right:
                return left

            mid = (right - left) // 2 + left
            
            if isBadVersion(mid):
                return firstBadVersion(left, mid)
            
            return firstBadVersion(mid + 1, right)
       
        return firstBadVersion(1, n)
