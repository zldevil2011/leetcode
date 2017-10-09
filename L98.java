import java.util.ArrayList;
import java.util.List;
public class L98 {
	public class TreeNode {
		 int val;
		 TreeNode left;
		 TreeNode right;
		 TreeNode(int x) { val = x; }
	}
	List<Integer> list = new ArrayList<Integer>();
	public boolean isValidBST(TreeNode root) {
		if(root == null){
			return true;
		}
		if(root.left == null && root.right == null){
			return true;
		}
		
		inOrderTravel(root);
		int L = list.size();
		for(int i = 1; i < L; ++i){
			if(list.get(i) <= list.get(i-1)){
				return false;
			}
		}
		return true;
    }
	public void inOrderTravel(TreeNode root){
		if(root == null){
			return;
		}
		inOrderTravel(root.left);
		list.add(root.val);
		inOrderTravel(root.right);
	}
}
/*
 * 通过获取中序遍历结果看是否是排序的
 */
