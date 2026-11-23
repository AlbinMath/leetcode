
var diameterOfBinaryTree = function(root) {
    let diameter = 0;

    function height(node) {
        if (node === null) {
            return 0;
        }

        const leftHeight = height(node.left);
        const rightHeight = height(node.right);

        // Longest path through this node, measured in edges.
        diameter = Math.max(
            diameter,
            leftHeight + rightHeight
        );

        // Return the height of this subtree.
        return 1 + Math.max(leftHeight, rightHeight);
    }

    height(root);

    return diameter;
};

