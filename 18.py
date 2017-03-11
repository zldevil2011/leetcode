class Solution(object):
	def fourSum(self, nums, target):
		length = len(nums)
		if length < 4:
			return []
		res = []
		nums.sort()
		for i in range(length):
			# if i > 0 and nums[i] == nums[i-1]:
			# 	continue
			for j in range(i+1, length):
				# if j > 0 and nums[j] == nums[j-1]:
				# 	break
				left = j + 1
				right = length - 1
				while left < right:
					sum_4 = nums[i] + nums[j] + nums[left] + nums[right]
					if sum_4 == target:
						tmp = [nums[i], nums[j], nums[left], nums[right]]
						res.append(tmp)
						left += 1
						right -= 1
						while left < right and nums[left] == nums[left - 1]:
							left += 1
						while left < right and nums[right] == nums[right+1]:
							right -= 1
					elif sum_4 > target:
						right -= 1
					else:
						left += 1
		ret_res = []
		for r in res:
			if r not in ret_res:
				ret_res.append(r)
		return ret_res

if __name__ == '__main__':
	s = Solution()
	nums = [0,4,-5,2,-2,4,2,-1,4]
	target = 12
	print s.fourSum(nums, target)