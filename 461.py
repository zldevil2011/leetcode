class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xy = x ^ y
        ans = 0
        for i in range(0,32):
            tp = xy & 1
            ans += tp
            xy = xy >> 1
        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1,4))