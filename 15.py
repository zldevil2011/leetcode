class Solution(object):
	def threeSum(self, nums):
		length = len(nums)
		if length < 3:
			return []
		res = []
		nums.sort()
		for i in range(length):
			if nums[i] > 0:
				break
			if i > 0 and nums[i] == nums[i-1]:
				continue
			left = i + 1
			right = length - 1
			while left < right:
				sum_3 = nums[i] + nums[left] + nums[right]
				if sum_3 == 0:
					tmp = [nums[i], nums[left], nums[right]]
					res.append(tmp)
					left += 1
					right -= 1
					while left < right and nums[left] == nums[left - 1]:
						left += 1
					while left < right and nums[right] == nums[right+1]:
						right -= 1
				elif sum_3 > 0:
					right -= 1
				else:
					left += 1
		return res