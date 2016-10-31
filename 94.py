# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 非递归方法，从根节点开始一直把左孩子放进栈里，然后出栈，出完栈后指向右孩子，此时当前根节点已经出站，如此循环直至栈空
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        cur = root
        while cur != None or len(stack) > 0:
        	while cur != None:
        		stack.append(cur)
        		cur = cur.left
        	cur = stack[-1]
        	stack.pop()
        	result.append(cur.val)
        	cur = cur.right
        return result
# 递归的方法，先遍历左孩子，再根节点，在右孩子        
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.read(root, res)
        return res

    def read(self, root, result):
    	if root != None:
    		self.read(root.left, result)
    		result.append(root.val)
    		self.read(root.right, result)
        