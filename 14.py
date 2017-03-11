class Solution(object):
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ""
		aim = strs[0]
		Min = len(aim)
		for i in range (1, len(strs)):
			j = 0
			tmp = strs[i]
			while j < Min and j < len(tmp) and aim[j] == tmp[j]:
				j += 1
			if Min > j:
				Min = j
		return aim[:Min]