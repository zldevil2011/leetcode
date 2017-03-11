class Solution(object):
	def isValid(self, s):
		length = len(s)
		if length < 2:
			return False
		L = []
		L.append(s[0])
		step = 1
		for i in range(1, length):
			if s[i] == '(' or s[i] == '[' or s[i] == '{':
				L.append(s[i])
				step += 1
			elif s[i] == ')':
				try:
					if L[step-1] == '(':
						del L[step-1]
						step -= 1
					else:
						return False
				except:
					return False
			elif s[i] == '}':
				try:
					if L[step-1] == '{':
						del L[step-1]
						step -= 1
					else:
						return False
				except:
					return False
			elif s[i] == ']':
				try:
					if L[step-1] == '[':
						del L[step-1]
						step -= 1
					else:
						return False
				except:
					return False
		if len(L) > 0:
			return False
		return True

if __name__ == '__main__':
	s = Solution()
	print s.isValid("()[]{}")
	print s.isValid("(]")
	print s.isValid("([)]")
	print s.isValid("[]")
	print s.isValid("[])")