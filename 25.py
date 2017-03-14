# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		p = ListNode(0)
		p.next = head
		head = p
		s = p
		length = k
		while k > 0 and s is not None:
			k -= 1
			s = s.next
		while s is not None:
			flag = s.next
			tail = p.next
			l = p.next
			while l != flag:
				tmp = p.next
				p.next = l
				l = l.next
				p.next.next = tmp
			tail.next = l
			p = tail
			s = tail
			k = length
			while k > 0 and s is not None:
				k -= 1
				s = s.next
		return head.next
