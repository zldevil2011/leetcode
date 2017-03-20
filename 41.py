class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 1
		i = 0
		while i < len(nums):
			if len(nums) >= nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
				tmp = nums[nums[i] - 1]
				nums[nums[i] - 1] = nums[i]
				nums[i] = tmp
				i -= 1
			i+=1
		i = 0
		while i < len(nums):
			if nums[i] != i + 1:
				return i + 1
			i += 1
		return len(nums) + 1

if __name__ == '__main__':
	nums = [2]
	s = Solution()
	print(s.firstMissingPositive(nums))