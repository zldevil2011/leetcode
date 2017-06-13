class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		order_list = path.split('/')
		stack = []
		s_len = 0
		for order in order_list:
			if order == ".":
				pass
			elif order == "..":
				if len(stack) > 0:
					stack.pop()
			elif len(order) > 0:
				stack.append(order)
		res = "/"
		for order in stack:
			res += order + "/"
		if len(res) > 1:
			res = res[:-1]
		return res

if __name__ == '__main__':
	s = Solution()
	print s.simplifyPath("/home/")
	print s.simplifyPath("/a/./b/../../c/")
	print s.simplifyPath("/")
	print s.simplifyPath("/..")