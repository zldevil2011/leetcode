class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		fg = 0
		if dividend > 0 and divisor > 0:
			fg = 1
		elif dividend < 0 and divisor < 0:
			fg = 1
		if dividend == 0:
			return 0
		dividend = abs(dividend)
		divisor = abs(divisor)
		map = [0 for i in range(33)]
		times = [1 for i in range(33)]
		i = 0
		map[0] = divisor
		times[0] = 1
		while map[i] <= dividend:
			i += 1
			map[i] = map[i-1] + map[i-1]
			times[i] = times[i-1] + times[i-1]
		j = i-1
		sum = 0
		while j >= 0:
			while map[j] <= dividend:
				dividend -= map[j]
				sum += times[j]
			j -= 1
		sum = -sum if fg == 0 else sum
		if sum > 2147483647:
			return 2147483647
		else:
			return sum

