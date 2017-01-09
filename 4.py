class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		n = len(nums1)
		m = len(nums2)
		res = self.merge(nums1, nums2)
		return (res[(m+n-1)/2] + res[(m+n)/2]) / 2.0
	def merge(self, nums1, nums2):
		res = []
		n = len(nums1)
		m = len(nums2)
		i = 0
		j = 0
		while i < n and j < m:
			if nums1[i] <= nums2[j]:
				res.append(nums1[i])
				i += 1
			else:
				res.append(nums2[j])
				j += 1
		if i == n:
			while j < m:
				res.append(nums2[j])
				j += 1
		if j == m:
			while i < n:
				res.append(nums1[i])
				i += 1
		return res

if __name__ == '__main__':
	s = Solution()
	print s.findMedianSortedArrays([1,2], [3,4])