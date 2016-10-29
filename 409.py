#!/usr/bin/env python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        ll = len(s)
        num = []
        for i in range(58):
        	num.append(0)
        ans = 0
        for i in range(ll):
        	idx = ord(s[i]) - 65
        	num[idx] += 1
        	if num[idx] == 2:
        		ans += 2
        		num[idx] = 0
        for i in range(58):
        	if num[i] == 1:
        		ans += 1
        		break
        return ans

if __name__ == '__main__':
	s = Solution()
	ss = 'abccccdd'
	print s.longestPalindrome(ss)