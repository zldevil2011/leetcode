class Solution(object):
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		candidates.sort()
		self.re = []
		self.dfs(candidates, target, 0, [])
		return self.re

	def dfs(self, candidates, target, start, val):
		if target == 0 and val not in self.re:
			self.re.append(val)
		else:
			for i in range(start, len(candidates)):
				if target < candidates[i]:
					break
				else:
					self.dfs(candidates, target - candidates[i], i + 1, val + [candidates[i]])

if __name__ == '__main__':
	s = Solution()
	candidates = [10, 1, 2, 7, 6, 1, 5]
	target = 8
	print s.combinationSum2(candidates, target)