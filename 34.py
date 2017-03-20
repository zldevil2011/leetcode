class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		res = [-1,-1]
		if nums is None or len(nums) == 0:
			return res
		low = 0
		high = len(nums) - 1
		pos = 0
		while low <= high:
			mid = (low + high) / 2
			pos = mid
			if nums[mid] > target:
				high = mid - 1
			elif nums[mid] < target:
				low = mid + 1
			else:
				res[0] = pos
				res[1] = pos
				break
		if nums[pos] != target:
			return res
		new_low = pos
		new_high = len(nums) - 1
		while new_low <= new_high:
			new_mid = (new_low + new_high) / 2
			if nums[new_mid] == target:
				new_low = new_mid + 1
			else:
				new_high = new_mid - 1
		res[1] = new_high
		new_low = 0
		new_high = pos
		while new_low <= new_high:
			new_mid = (new_high + new_low) / 2
			if nums[new_mid] == target:
				new_high = new_mid - 1
			else:
				new_low = new_mid + 1
		res[0] = new_low
		return res