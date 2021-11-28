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
 * @return {number}
 */

let minDepthHelper = function(root, depth) {
        if (root.left === null && root.right === null) {
            return 1;
        } else if (root.left === null) {
            return 1 + minDepthHelper(root.right, depth)
        } else if (root.right === null) {
            return 1 + minDepthHelper(root.left, depth)
        } else {
            return 1 + Math.min(minDepthHelper(root.left, depth), minDepthHelper(root.right, depth));
        }
}
let minDepth = function(root) {
    let lowestDepth = 0;
    if (root) {
        lowestDepth = minDepthHelper(root, 0);
    }
    console.log(lowestDepth)
    return lowestDepth;
};