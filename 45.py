class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		idx = 0
		cnt = 0
		lst = 0
		rea = 0
		while rea >= idx and idx < len(nums):
			if lst < idx:
				cnt += 1
				lst = rea
			rea = max(rea, nums[idx] + idx)
			idx += 1
		if rea < len(nums) - 1:
			return 0
		return cnt

if __name__ == '__main__':
	s = Solution()
	nums = [2,3,1,1,4]
	print(s.jump(nums))
