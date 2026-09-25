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
var averageOfSubtree = function(root) {
    let count = 0;

    function dfs(node) {
        if (node === null) {
            return [0, 0]; // [sum, number of nodes]
        }

        let [leftSum, leftCount] = dfs(node.left);
        let [rightSum, rightCount] = dfs(node.right);

        let sum = leftSum + rightSum + node.val;
        let nodes = leftCount + rightCount + 1;

        // Average is rounded down
        if (Math.floor(sum / nodes) === node.val) {
            count++;
        }

        return [sum, nodes];
    }

    dfs(root);

    return count;
};
