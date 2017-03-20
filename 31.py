class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		length = len(nums)
		i = length - 1
		while i > 0 and nums[i] <= nums[i - 1]:
			i -= 1
		if i > 0:
			j = length - 1
			while nums[j] <= nums[i-1]:
				j -= 1
			tmp = nums[j]
			nums[j] = nums[i-1]
			nums[i-1] = tmp
		j = length - 1
		while i < j:
			tmp = nums[i]
			nums[i] = nums[j]
			nums[j] = tmp
			i += 1
			j -= 1

if __name__ == '__main__':
	s = Solution()
	s.nextPermutation([1,2])