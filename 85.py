class Solution(object):
	def generate(self, matrix, row, heights):
		col = len(matrix[0])
		for i in range(col):
			if matrix[row][i] == '0':
				heights[i] = 0
			else:
				heights[i] = heights[i] + 1
	def maximalRectangle(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return 0

		ron_no = len(matrix)
		ans = 0
		heights = [0 for i in range(len(matrix[0]))]
		for i in range(ron_no):
			self.generate(matrix, i, heights)
			ans = max(ans, self.largestRectangleArea(heights))
		return ans
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
    
    
    
# 类似于84题，把85题可以转换成84题，对于每一行，求当前行到首行的直方图的最大矩阵（构建矩阵时，相连的1可以组成直方图，如果是0，则直接为0，断开和前面行数据的链接）
