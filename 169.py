# !/usr/bin/env python
class Solution(object):
	def majorityElement(self, nums):
		ll = len(nums)
		if ll == 1:
			return nums[0]
		pre = nums[0]
		rep_no = 1
		for i in range(1,ll):
			if rep_no == 0:
				pre = nums[i]
				rep_no = 1
			else:
				if nums[i] == pre:
					rep_no += 1
				else:
					rep_no -= 1

		return pre

if __name__ == '__main__':
	s = Solution()
	ss = '655'
	ss = [10,9,9,9,10]
	print s.majorityElement(ss)
