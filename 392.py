class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        ls = len(s)
        t = list(t)
        lt = len(t)
        ids = 0
        idt = 0
        while ids < ls and idt < lt:
        	if s[ids] == t[idt]:
        		ids += 1
        	idt += 1
        return ids == ls

if __name__ == '__main__':
	s = Solution()
	ss = ''
	tt = 'ahbgdc'
	print s.isSubsequence(ss,tt)