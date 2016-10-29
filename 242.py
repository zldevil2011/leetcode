#!/usr/bin/env python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        num = []
        for i in range(26):
        	num.append(0)
        # print num
        s = list(s)
        t = list(t)
        for i in range(len(s)):
        	idx = ord(s[i]) - 97
        	# print idx
        	num[idx] += 1
        for i in range(len(t)):
        	idx = ord(t[i]) - 97
        	num[idx] -= 1
        for i in range(26):
        	if num[i] != 0:
        		return False
        return True

if __name__ == '__main__':
	s = Solution()
	ss = 'anagram'
	tt = 'nagaram'
	print s.isAnagram(ss,tt)
