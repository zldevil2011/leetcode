class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
        	return 0
        ret = self.s2i(s[0])
        lenS = len(s)
        for i in range(1, lenS):
        	NEW = self.s2i(s[i])
        	OLD = self.s2i(s[i-1])
        	if NEW > OLD:
        		ret += (NEW - 2 * OLD)
        	else:
        		ret += NEW
        return ret

    def s2i(self, c):
    	if c == "I":
    		return 1
    	if c == "V":
    		return 5
    	if c == "X":
    		return 10
    	if c == "L":
    		return 50
    	if c == "C":
    		return 100
    	if c == "D":
    		return 500
    	if c == "M":
    		return 1000
    	return 0

if __name__ == '__main__':
	s = Solution()
	st1 = 'IV'
	print s.romanToInt(st1)