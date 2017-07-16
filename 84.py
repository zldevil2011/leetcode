class Solution(object):
	def largestRectangleArea(self, heights):
		"""
		:type heights: List[int]
		:rtype: int
		"""
		ret = 0
		stk = []
		p_no = 0
		for i in range(0, len(heights)):
			if len(stk) == 0 or stk[len(stk)-1] <= heights[i]:
				stk.append(heights[i])
			else:
				count = 0
				while len(stk) > 0 and (stk[len(stk)-1] > heights[i]):
					count += 1
					ret = max(ret, stk[len(stk)-1] * count)
					stk.pop()
				while count > 0:
					stk.append(heights[i])
					count -= 1
				stk.append(heights[i])
		cnt = 1
		while len(stk) > 0:
			ret = max(ret, stk[len(stk)-1]*cnt)
			stk.pop()
			cnt += 1
		return ret
    
    
#http://www.cnblogs.com/ganganloveu/p/4148303.html
