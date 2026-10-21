
var pathSum = function(root, targetSum) {
    const prefixCount = new Map();
    prefixCount.set(0, 1);

    let count = 0;

    function dfs(node, currentSum) {
        if (node === null) {
            return;
        }

        currentSum += node.val;

        // Find paths ending at this node with the target sum.
        const needed = currentSum - targetSum;
        count += prefixCount.get(needed) || 0;

        // Add the current prefix sum before visiting children.
        prefixCount.set(
            currentSum,
            (prefixCount.get(currentSum) || 0) + 1
        );

        dfs(node.left, currentSum);
        dfs(node.right, currentSum);

        // Backtrack: remove this prefix sum for other branches.
        prefixCount.set(
            currentSum,
            prefixCount.get(currentSum) - 1
        );
    }

    dfs(root, 0);

    return count;
};

