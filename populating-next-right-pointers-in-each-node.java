/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
		if (root == null)
			return;
		Queue<TreeLinkNode> q1 = new LinkedList<TreeLinkNode>();
		Queue<TreeLinkNode> q2 = new LinkedList<TreeLinkNode>();
		q1.add(root);
		while (!q1.isEmpty()) {
			TreeLinkNode tmp = q1.poll();
			if (tmp.left != null)
				q2.add(tmp.left);
			if (tmp.right != null)
				q2.add(tmp.right);
			if (q1.isEmpty()) {
				q1 = q2;
				tmp.next = null;
				q2 = new LinkedList<TreeLinkNode>();
			} else {
				tmp.next = q1.peek();
			}
		}       
    }
}