import sys
class Solution(object):
	def maxSubArray1(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		def max_s(nums, i, j):
			if i == j:
				return nums[i]
			m = (i + j) / 2
			l = max_s(nums, i, m)
			r = max_s(nums, m + 1, j)
			lm = -1 * sys.maxint
			rm = -1 * sys.maxint
			s = 0
			for k in range(m, i-1, -1):
				s += nums[k]
				if s > lm:
					lm = s
			s = 0
			for k in range(m+1, j+1):
				s += nums[k]
				if s > rm:
					rm = s
			return max(l, max(r, lm+rm))
		if len(nums) == 1:
			return nums[0]
		return max_s(nums, 0, len(nums) - 1)

	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		s = nums[len(nums) - 1]
		max_s = s
		for i in range(len(nums) - 2, -1, -1):
			s = max(nums[i], s + nums[i])
			print s
			max_s = max(max_s, s)
		return max_s

if __name__ == '__main__':
	# nums = [-2,1,-3,4,-1,2,1,-5,4]
	nums = [-1, -2]
	s = Solution()
	print s.maxSubArray(nums)