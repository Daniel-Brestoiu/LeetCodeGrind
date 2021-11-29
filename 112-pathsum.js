/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
 let addValues = function(root, currentSum, targetSum) {
    let leftLeaf = false;
    let rightLeaf = false;
    if (root.left != null) {
        leftLeaf = addValues(root.left, currentSum + root.val, targetSum);
    } 
    if (root.right != null) {
        rightLeaf = addValues(root.right, currentSum + root.val, targetSum);
    }
    
    if (root.left == null && root.right == null) {
        //Must be on a leaf right now.
        return (root.val + currentSum == targetSum);
    } else {
        return (leftLeaf || rightLeaf);
    }
}

let hasPathSum = function(root, targetSum) {
    if (root == null) return false;
    return addValues(root, 0, targetSum);
};