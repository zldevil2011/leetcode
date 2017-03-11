# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		left=right=head
		for i in range(n):
			right=right.next
		if right is None:
			return head.next    #special
		while right.next is not None:
			right=right.next
			left=left.next

		left.next=left.next.next
		return head
if __name__  == '__main__':
	a = ListNode(1)
	b = ListNode(2)
	a.next = b
	b.next = None

	s = Solution()
	print s.removeNthFromEnd(a, 1)