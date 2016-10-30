import math
class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        mini = max(0, num - 6)
        maxi = min(4, num)
        for i in range(mini, maxi + 1):
        	vec1 = []
        	vec2 = []
        	self.DFS(4, i, 0, 0, vec1)
        	self.DFS(6, num - i, 0, 0, vec2)
        	for h in vec1:
        		for m in vec2:
        			if m < 10:
        				minute = "0" + str(int(m))
        			else:
        				minute = str(int(m))
        			hour = str(int(h)) + ":"
        			res.append(hour + minute)
        return res
    def DFS(self, lenP, k, curIndex, val, arr):
    	if k == 0 and lenP == 4 and val < 12:
    		arr.append(val)
    	if k == 0 and lenP == 6 and val < 60:
    		arr.append(val)
    	if curIndex == lenP or k == 0:
    		return
    	self.DFS(lenP, k, curIndex + 1, val, arr)
    	val += math.pow(2, curIndex)
    	k -= 1
    	curIndex += 1
    	self.DFS(lenP, k, curIndex, val, arr)

if __name__ == '__main__':
	s = Solution()
	n = 1
	print s.readBinaryWatch(n)