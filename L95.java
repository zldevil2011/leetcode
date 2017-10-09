import java.util.ArrayList;
import java.util.List;
public class L95 {
	public class TreeNode {
		int val;		 
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	public List<TreeNode> generateTrees(int n){
		List<TreeNode> t = new ArrayList<TreeNode>();
		if(n < 1){
			return t;
		}
		return cal(1, n);
	}
	public List<TreeNode> cal(int start, int end){
		List<TreeNode> res = new ArrayList<TreeNode>();
		if(start > end){
			res.add(null);
			return res;
		}
		for(int i = start; i <= end; ++i){
			List<TreeNode> lefts = cal(start, i - 1);
			List<TreeNode> rights = cal(i+1, end);
			for(TreeNode left : lefts){
				for(TreeNode right : rights){
					TreeNode root = new TreeNode(i);
					root.left = left;
					root.right = right;
					res.add(root);
				}
			}
			
		}
		return res;
	}
	public static void main(String[] args){
		L95 l = new L95();
		List<TreeNode> ans = l.generateTrees(3);
		System.out.println(ans.size());
	}
}
/*
1. 选出根结点后应该先分别求解该根的左右子树集合，也就是根的左子树有若干种，它们组成左子树集合，根的右子树有若干种，它们组成右子树集合。 
2. 然后将左右子树相互配对，每一个左子树都与所有右子树匹配，每一个右子树都与所有的左子树匹配。然后将两个子树插在根结点上。 
3. 最后，把根结点放入链表中。
*/
