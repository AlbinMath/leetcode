
var sumNumbers = function(root) {
    let total = 0;

    function dfs(node, currentNumber) {
        if (node === null) {
            return;
        }

        currentNumber = currentNumber * 10 + node.val;

        // Check if this is a leaf node
        if (node.left === null && node.right === null) {
            total += currentNumber;
            return;
        }

        dfs(node.left, currentNumber);
        dfs(node.right, currentNumber);
    }

    dfs(root, 0);

    return total;
};

