class Solution(object):
	def convert(self, s, numRows):
		if numRows <= 1 or len(s) <= 2:
			return s
		row_str = ["" for i in range(numRows)]
		count = 2 * (numRows - 1)
		for i in range(len(s)):
			row_str[numRows - 1 - abs(numRows - 1 - (i % count))] += s[i]
		ans = ""
		for i in row_str:
			ans += i
		return ans

if __name__ == '__main__':
	S = Solution()
	print S.convert("PAYPALISHIRING", 3)