class Solution(object):
	def subsets(self, nums):
		'''
		:param nums: List[int]
		:return: List[List[int]]
		'''
		total = 1 << len(nums)
		ans = []
		for i in range(total):
			poi = bin(i).replace("0b", "")
			poi = list(poi)
			poi.reverse()
			l = len(poi)
			tmp = []
			for j in range(l):
				if poi[j] == '1':
					tmp.append(nums[j])
			ans.append(tmp)
		return ans
if __name__ == '__main__':
	s = Solution()
	print(s.subset([1,2,3]))