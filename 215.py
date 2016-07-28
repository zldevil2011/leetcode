#!/usr/bin/env python
class Solution(object):
	def __init__(self):
		self.nums_t = []
	def min_heap(self, i, l):
		L = i * 2
		R = i * 2 + 1
		large = i
		# print "** = ", self.nums_t[i-1]
		if L <= l and self.nums_t[L-1] < self.nums_t[i-1]:
			# print  "L>",  self.nums_t[L-1]
			large = L
		if R <= l and self.nums_t[R-1] < self.nums_t[large-1]:
			# print  "R>",  self.nums_t[R-1]
			large = R
		# print "i = " , i , " large = ", large
		if large != i:
			tp = self.nums_t[large-1]
			self.nums_t[large-1] = self.nums_t[i-1]
			self.nums_t[i-1] = tp
			self.min_heap(large, l)

	def build_min_heap(self):
		l = len(self.nums_t)
		for i in range(l/2, 0, -1):
			self.min_heap(i, l)

	def findKthLargest(self, nums, k):
		self.nums_t = nums[0:k]
		# print self.nums_t
		self.build_min_heap()
		nums_leave = nums[k:]
		LL = len(nums_leave)
		for i in range(0, LL):
			if nums_leave[i] > self.nums_t[0]:
				self.nums_t[0] = nums_leave[i]
				self.min_heap(1, len(self.nums_t))
		return self.nums_t[0]

if __name__ == '__main__':
	nums = [4,1,3,2,16,9,10,14,8,7]
	l = 5
	s = Solution()
	ans = s.findKthLargest(nums, l)
	print "ans : ", ans
	# for i in range(0,l):
	# 	print s.nums_t[i]

