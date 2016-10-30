
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))
if __name__ == '__main__':
	s = Solution()
	ss = []
	print s.containsDuplicate(ss)
        