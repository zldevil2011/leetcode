class Solution(object):
	def letterCombinations(self, digits):
		if digits == "":
			return []
		res = []
		res.append("")
		dict = {}
		dict[2] = "abc"
		dict[3] = "def"
		dict[4] = "ghi"
		dict[5] = "jkl"
		dict[6] = "mno"
		dict[7] = "pqrs"
		dict[8] = "tuv"
		dict[9] = "wxyz"
		for i in range(len(digits)):
			s = len(res)
			for j in range(s):
				cur = res[0]
				del res[0]
				for k in range(len(dict[int(digits[i])])):
					res.append(str(cur) + dict[int(digits[i])][k])

		return res
