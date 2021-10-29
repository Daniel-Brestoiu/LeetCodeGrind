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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    //Can ignore root value.  
    //If left and right are equal, then is equal.
    if (root == null ) {
        return true;
    }
    return isSymmetricHelper(root.left, root.right);
};

var isSymmetricHelper = function(rootL, rootR) {
    console.log(rootL, rootR)
    if (rootL === null && rootR === null) {
        return true;
    } else if (rootL === null || rootR === null) {
        //One is null, other isnt.
        return false;
    }
    let sameValue = (rootL.val == rootR.val);
    if (!sameValue) {
        return false;
    }
    let sameLeft = isSymmetricHelper(rootL.left, rootR.right);
    if (!sameLeft) {
        return false;
    }
    let sameRight = isSymmetricHelper(rootL.right, rootR.left);
    return sameRight;
};