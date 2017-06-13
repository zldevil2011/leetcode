class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0:
			return []
		ret = []
		start_x = 0
		start_y = 0
		n = len(matrix)
		m = len(matrix[0])
		visit = []
		for i in range(n):
			visit.append([0 for j in range(m)])
		direction = 0
		while True:
			if visit[start_x][start_y] == 0:
				visit[start_x][start_y] = 1
				ret.append(matrix[start_x][start_y])
			if len(ret) == n * m:
				break
			if direction == 0 and start_y + 1 < m and visit[start_x][start_y+1] == 0:
				start_y += 1
				continue
			elif direction == 0:
				direction = 1
				continue
			if direction == 1 and start_x + 1 < n and visit[start_x + 1][start_y] == 0:
				start_x += 1
				continue
			elif direction == 1:
				direction = 2
				continue
			if direction == 2 and start_y - 1 >= 0 and visit[start_x][start_y-1] == 0:
				start_y -= 1
				continue
			elif direction == 2:
				direction = 3
				continue
			if direction == 3 and start_x - 1 >= 0 and visit[start_x-1][start_y] == 0:
				start_x -= 1
				continue
			elif direction == 3:
				direction = 0
				continue
		return ret

if __name__ == "__main__":
	s = Solution()
	matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	s.spiralOrder(matrix)