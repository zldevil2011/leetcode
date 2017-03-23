class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def _(result, temp, nums):
			if nums == []:
				result += [temp]
			else:
				for i in range(len(nums)):
					if i > 0 and nums[i] == nums[i-1]:
						continue
					_(result, temp + [nums[i]], nums[:i] + nums[i+1:])
		if nums is None:
			return []
		if len(nums) == 0:
			return [[]]
		result = []
		_(result, [], sorted(nums))
		return result

if __name__ == '__main__':
	nums = [1,1,2]
	s = Solution()
	print s.permuteUnique(nums)