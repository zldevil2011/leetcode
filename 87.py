class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
        	return False
        if s1 == s2:
        	return True
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 != l2:
        	return False
        l_e = len(s1)
        for i in range(1,l_e):
        	if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        		return True
        	if self.isScramble(s1[:i],s2[l_e-i:]) and self.isScramble(s1[i:],s2[:l_e-i]):
        		return True
       	return False
        
    # 递归求解字串是不是scrambled
