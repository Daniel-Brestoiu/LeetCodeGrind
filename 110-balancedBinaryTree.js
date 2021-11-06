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

let isBalanced = function(root) {
    let getDepth = function(root) {
        if (root != undefined) {
            let ldepth = 1;
            let rdepth = 1;
            if (root.left) {
                ldepth = 1 + getDepth(root.left);
            }
            if (root.right) {
                rdepth = 1 + getDepth(root.right);
            }
            return Math.max(ldepth, rdepth);
            
        } else {
            return 0;
        }
    }
    
    let comparator = function(root) {
        if (root) {
            ldepth = getDepth(root.left);
            rdepth = getDepth(root.right);
            if (Math.abs(ldepth - rdepth) <= 1) {
                return true;
            } else {
                return false;
            }
        }
        return true;
    }
    
    let compHelp = function(root) {
        if (root) {
            return (compHelp(root.left) && compHelp(root.right) && comparator (root));
        }
        return true;
    }
    
    return compHelp(root);
};