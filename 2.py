class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		ret = ListNode(0)
		pot = ret
		add = 0
		while l1 is not None or l2 is not None:
			if l1 is not None:
				add += l1.val
				l1 = l1.next
			if l2 is not None:
				add += l2.val
				l2 = l2.next
			pot.next = ListNode(add % 10)
			add /= 10
			pot = pot.next
		if add > 0:
			pot.next = ListNode(add)
		return ret.next


if __name__ == '__main__':
	s = Solution()
	print "test"