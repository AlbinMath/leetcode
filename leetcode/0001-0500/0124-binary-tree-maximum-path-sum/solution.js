
var maxPathSum = function(root) {
    let maxSum = -Infinity;

    function dfs(node) {
        if (node === null) {
            return 0;
        }

        // Ignore negative contributions
        const leftGain = Math.max(0, dfs(node.left));
        const rightGain = Math.max(0, dfs(node.right));

        // Maximum path passing through this node
        const pathSum = node.val + leftGain + rightGain;

        maxSum = Math.max(maxSum, pathSum);

        // Return the best single branch to the parent
        return node.val + Math.max(leftGain, rightGain);
    }

    dfs(root);

    return maxSum;
};

