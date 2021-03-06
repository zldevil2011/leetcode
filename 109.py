"""
109
递归的执行，将当前列表中间的位置的数字作为根节点，然后递归的处理左半部分作为左孩子，右半部分作为右孩子
"""
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		list_len = 0
		tmp = head
		while tmp is not None and tmp.next is not None:
			list_len += 1
			tmp = tmp.next
		if tmp is not None:
			list_len += 1
		if list_len == 0:
			return None
		elif list_len == 1:
			return TreeNode(head.val)
		elif list_len == 2:
			child = TreeNode(head.next.val)
			head = TreeNode(head.val)
			head.right = child
			return head
		else:
			left_len = list_len / 2
			right_len = list_len - left_len - 1
			left_head = head
			step = 0
			pre_node = None
			while step < left_len:
				step += 1
				pre_node = head
				head = head.next
			pre_node.next = None
			root = TreeNode(head.val)
			right_head = head.next
			tmp = right_head
			step += 1
			while step < list_len:
				step += 1
				tmp = tmp.next
			root.left = self.sortedListToBST(left_head)
			root.right = self.sortedListToBST(right_head)
			return root

if __name__ == '__main__':
	s = Solution()
	head = ListNode(-10)
	node2 = ListNode(-3)
	node3 = ListNode(0)
	node4 = ListNode(5)
	node5 = ListNode(9)
	head.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	tree = s.sortedListToBST(head)
