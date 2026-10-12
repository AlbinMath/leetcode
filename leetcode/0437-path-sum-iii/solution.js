
var pathSum = function(root, targetSum) {
    const prefixSum = new Map();
    prefixSum.set(0, 1);

    function dfs(node, currentSum) {
        if (node === null) {
            return 0;
        }

        currentSum += node.val;

        let count = prefixSum.get(currentSum - targetSum) || 0;

        prefixSum.set(
            currentSum,
            (prefixSum.get(currentSum) || 0) + 1
        );

        count += dfs(node.left, currentSum);
        count += dfs(node.right, currentSum);

        prefixSum.set(
            currentSum,
            prefixSum.get(currentSum) - 1
        );

        return count;
    }

    return dfs(root, 0);
};

