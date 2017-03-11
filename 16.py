class Solution(object):
	def threeSumClosest(self, nums, target):
		length = len(nums)
		Min = 2147483647
		nums.sort()
		for i in range(length):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			left = i + 1
			right = length - 1
			while left < right:
				sum_3 = nums[i] + nums[left] + nums[right]
				if abs(sum_3 - target) < abs(Min):
					Min = sum_3 - target
				if sum_3 == target:
					return target
				elif sum_3 > target:
					right -= 1
				else:
					left += 1
		return Min + target