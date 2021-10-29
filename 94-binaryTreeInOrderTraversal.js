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
 * @return {number[]}
 */
 var inorderTraversal = function(root) {
    let array = []
    inorderTraversalHelper(root, array);
    return array;
};

var inorderTraversalHelper = function(root, array) {
    if (root) {
        //Left
        if (root.left !== null) {
            array = inorderTraversalHelper(root.left, array);
        }

        //Take current put in array
        if (root.val !== null) {
            let value = root.val
            array.push(value);
        }

        //Right
        if (root.right !== null) {
            array = inorderTraversalHelper(root.right, array);
        }
    }
    return array;
    
};