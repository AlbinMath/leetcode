
var longestZigZag = function(root) {
    let maxLength = 0;

    function dfs(node, leftLength, rightLength) {
        if (node === null) {
            return;
        }

        maxLength = Math.max(maxLength, leftLength, rightLength);

        if (node.left) {
            dfs(node.left, rightLength + 1, 0);
        }

        if (node.right) {
            dfs(node.right, 0, leftLength + 1);
        }
    }

    dfs(root, 0, 0);

    return maxLength;
};

