
var countNodes = function(root) {
    if (root === null) {
        return 0;
    }

    let left = root.left;
    let right = root.right;
    let leftHeight = 0;
    let rightHeight = 0;

    while (left !== null) {
        leftHeight++;
        left = left.left;
    }

    while (right !== null) {
        rightHeight++;
        right = right.right;
    }

    // If both heights are equal, the tree is perfect
    if (leftHeight === rightHeight) {
        return Math.pow(2, leftHeight + 1) - 1;
    }

    // Otherwise, count recursively
    return 1 + countNodes(root.left) + countNodes(root.right);
};

