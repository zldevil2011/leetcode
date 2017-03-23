class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		dic, ans = {}, []
		for st in strs:
			o_str = ''.join(sorted(st))
			if o_str in dic:
				dic[o_str] += [st]
			else:
				dic[o_str] = [st]
		for i in dic:
			tmp = dic[i]
			tmp.sort()
			ans += [tmp]
		return ans

if __name__ == '__main__':
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	s = Solution()
	print s.groupAnagrams(strs)