#!/usr/bin/env python
class Solution(object):
	def combinationSum4(self, nums, target):
		dp = []
		for i in range(target+1):
			dp.append(0)
			print i
			for k in range(len(nums)):
				if i > nums[k]:
					dp[i] += dp[i - nums[k]]
				elif i == nums[k]:
					dp[i] += 1
		return dp[target]

if __name__ == '__main__':
	s = Solution()
	nums = [1,3,2]
	target = 4
	print s.combinationSum4(nums, 4)