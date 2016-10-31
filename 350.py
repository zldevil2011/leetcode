class Solution(object):
	def intersect(self, nums1, nums2):
		res = []
		for i in nums1:
			if i in nums2:
				res.append(i)
				nums2.remove(i)
		return res

if __name__ =='__main__':
	s = Solution()
	st = [1,2,2,4]
	ed = [3,2,2,5]
	print s.intersect(st, ed)