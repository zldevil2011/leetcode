class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if len(num1) > len(num2):
			return self.multiply(num2, num1)
		num1 = num1[::-1]
		num2 = num2[::-1]
		ans = [0] * (len(num1) * len(num2))
		for i in range(len(num1)):
			for j in range(len(num2)):
				ans[i + j] += int(num1[i]) * int(num2[j])
		c = 0
		for i in range(len(ans)):
			ans[i] += c
			ans[i], c = ans[i] % 10, ans[i] / 10
		while c > 0:
			ans.append(c%10)
			c /= 10
		idx = len(ans) - 1
		while idx > 0 and ans[idx] == 0:
			idx -= 1
		return ''.join([str(x) for x in ans[0:idx+1]][::-1])


if __name__ == '__main__':
	s = Solution()
	print s.multiply("2","3")