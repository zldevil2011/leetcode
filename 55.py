class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		# l = len(nums)
		# reach = [0 for i in range(l)]
		# reach[0] = 1
		# for i in range(l):
		# 	if reach[i] == 1:
		# 		end = min(i + nums[i] + 1, l)
		# 		for j in range(i+1, end):
		# 			reach[j] = 1
		#
		# if reach[l-1] == 1:
		# 	return True
		# else:
		# 	return False
		right_node = 1
		l = len(nums)
		for i in range(l):
			if right_node <= i:
				break
			right_node = max(right_node, i + nums[i] + 1)
		return right_node >= l
		# size = len(nums)
		# left = 0
		# right = 0
		# while left <= right:
		# 	pre_left = left
		# 	pre_right = right
		# 	for i in range(left, right + 1):
		# 		next_pos = nums[i] + i
		# 		if next_pos >= size - 1:
		# 			return True
		# 		if next_pos > right:
		# 			right = next_pos
		# 	left = pre_right
		# 	if left == pre_left and right == pre_right:
		# 		return False
		# return False


if __name__ == "__main__":
	s = Solution()
	nums = [0,1]
	print s.canJump(nums)