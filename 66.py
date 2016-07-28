#!/usr/bin/env python
class Solution(object):
	def plusOne(self, digits):
		'''
		:types digits:list[int]
		:rtype: List[int]
		'''
		Pl = len(digits)
		digits.reverse()
		x = int(digits[0]) + 1
		tmp = 0
		if x >= 10:
			tmp = x / 10
			digits[0] = x % 10
		else:
			tmp = 0
			digits[0] = x
		for i in range(1,Pl):
			x = digits[i] + tmp
			if x >= 10:
				tmp = 1
				digits[i] = x % 10
			else:
				tmp = 0
				digits[i] = x
		ans = []
		if tmp == 1:
			ans = digits + [1]
		else:
			ans = digits
		ans.reverse()
		return ans

if __name__ == '__main__':
	S = Solution()
	print S.plusOne([9,9,9])