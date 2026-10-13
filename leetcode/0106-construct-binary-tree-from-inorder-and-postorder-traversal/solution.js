
var buildTree = function(inorder, postorder) {
    const inorderMap = new Map();

    for (let i = 0; i < inorder.length; i++) {
        inorderMap.set(inorder[i], i);
    }

    let postorderIndex = postorder.length - 1;

    function build(left, right) {
        if (left > right) {
            return null;
        }

        const rootValue = postorder[postorderIndex--];
        const root = new TreeNode(rootValue);

        const mid = inorderMap.get(rootValue);

        // Build right subtree first
        root.right = build(mid + 1, right);
        root.left = build(left, mid - 1);

        return root;
    }

    return build(0, inorder.length - 1);
};

