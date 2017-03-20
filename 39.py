class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		self.re = []
		self.dfs(candidates, target, 0, [])
		return self.re

	def dfs(self, candidates, target, start, val):
		if target == 0:
			self.re.append(val)
		else:
			for i in range(start, len(candidates)):
				if target < 0:
					break
				else:
					self.dfs(candidates, target - candidates[i], i, val + [candidates[i]])

if __name__ == '__main__':
	s = Solution()
	candidates = [2,3,6,7]
	target = 7
	print s.combinationSum(candidates, target)
