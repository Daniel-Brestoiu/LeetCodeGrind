/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
 
class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        if let node = root {
            return maxDepthHelper(root: root, depth: 1);        
        } else {
            return 0;
        }
    }
    
    func maxDepthHelper(root: TreeNode?, depth: Int) -> Int {
        var leftDepth = depth;
        var rightDepth = depth;
        
        if let node = root {
            if (node.left != nil) {
                leftDepth = maxDepthHelper(root: node.left, depth: leftDepth) + 1;
            }
        } else {}
        if let node = root{
            if (node.right != nil) {
                rightDepth = maxDepthHelper(root: node.right, depth: rightDepth) + 1;
            }
        } else {}
        let maxSize = max(leftDepth, rightDepth);
        print(maxSize);
        return maxSize;
        
    }
}