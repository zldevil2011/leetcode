class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		pre = nums[:]
		nums.sort()
		start = 0
		end = len(nums) - 1
		ans = []
		while start <= end:
			tmp = nums[start] + nums[end]
			if tmp > target:
				end -= 1
			elif tmp < target:
				start += 1
			else:
				ans = [nums[start], nums[end]]
				break
		ret = []

		for i in ans:
			for index, tp in enumerate(pre):
				if i == tp:
					if len(ret) == 1 and ret[0] != index:
						ret.append(index)
						break
					elif len(ret) == 0:
						ret.append(index)
						break
		return ret

if __name__ == '__main__':
	s = Solution()
	print s.twoSum([0,4,3,0], 0)