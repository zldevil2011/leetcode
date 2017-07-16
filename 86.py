# 题目要求对链表分段，所有小于X的元素都排在大于等于X的前面。我是把小于X的值给取出来了，正确的应该是操作链表
# Definition for singly-linked list.
#class ListNode(object):
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		if head is None or head.next is None:
			return head
		t_list_left = []
		t_list_middle = []
		t_list_right = []
		while head is not None:
			if head.val < x:
				t_list_left.append(head.val)
			else:
				t_list_right.append(head.val)
			head = head.next

		if len(t_list_left) > 0:
			ans = ListNode(t_list_left[0])
			t = ans
			for i in range(1, len(t_list_left)):
				tmp = ListNode(t_list_left[i])
				t.next = tmp
				t = tmp
			for i in range(len(t_list_right)):
				tmp = ListNode(t_list_right[i])
				t.next = tmp
				t = tmp
			return ans
		else:
			ans = ListNode(t_list_right[0])
			t = ans
			for i in range(1, len(t_list_right)):
				tmp = ListNode(t_list_right[i])
				t.next = tmp
				t = tmp
			return ans
