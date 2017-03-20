class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		if n < 2:
			return 1
		ret_str = "1"
		while n > 1:
			temp, current_num = '', 0
			for i, v in enumerate(ret_str):
				if i > 0 and v != ret_str[i-1]:
					temp += str(current_num) + ret_str[i-1]
					current_num = 1
				else:
					current_num += 1
			ret_str = temp + (str(current_num) + ret_str[-1] if current_num != 0 else "")
			n -= 1
		return str(ret_str)


if __name__ == '__main__':
	s = Solution()
	print s.countAndSay(4)
	# for i in range(10):
	# 	print s.countAndSay(i)
