
var lowestCommonAncestor = function(root, p, q) {
    // Base case: empty node or either target found.
    if (root === null || root === p || root === q) {
        return root;
    }

    // Search for p and q in both subtrees.
    const left = lowestCommonAncestor(root.left, p, q);
    const right = lowestCommonAncestor(root.right, p, q);

    // Targets found in separate subtrees.
    if (left !== null && right !== null) {
        return root;
    }

    // Otherwise, return whichever subtree found a target.
    return left !== null ? left : right;
};

