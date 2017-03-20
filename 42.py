class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		left_most_high = [0 for i in range(len(height))]
		left_max = 0
		for i in range(len(height)):
			if height[i] > left_max:
				left_max = height[i]
			left_most_high[i] = left_max
		sum_total = 0
		right_max = 0
		for i in reversed(range(len(height))):
			if height[i] > right_max:
				right_max = height[i]
			if min(right_max, left_most_high[i]) > height[i]:
				sum_total += (min(right_max, left_most_high[i]) - height[i])
		return sum_total
