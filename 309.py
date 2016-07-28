#!/usr/bin/env python
class Solution(object):
	def maxProfit(self, prices):
		Plen = len(prices)
		if Plen < 2:
			return 0
		sell = [] 
		buy = []
		for i in range(Plen + 1):
			sell.append(0)
			buy.append(0)
		buy[0] = -prices[0]
		sell[-1] = 0
		for i in range(1,Plen):
			sell[i] = max(sell[i-1], buy[i-1] + prices[i])
			buy[i] = max(buy[i-1], sell[i-2] - prices[i])
		return sell[Plen-1]