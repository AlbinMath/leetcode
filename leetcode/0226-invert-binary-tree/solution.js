
var invertTree = function(root) {
    if (root === null) {
        return null;
    }

    // Swap the left and right children.
    const temp = root.left;
    root.left = root.right;
    root.right = temp;

    // Invert both subtrees.
    invertTree(root.left);
    invertTree(root.right);

    return root;
};

