
var buildTree = function(preorder, inorder) {
    const inorderMap = new Map();

    for (let i = 0; i < inorder.length; i++) {
        inorderMap.set(inorder[i], i);
    }

    let preorderIndex = 0;

    function build(left, right) {
        if (left > right) {
            return null;
        }

        const rootValue = preorder[preorderIndex++];
        const root = new TreeNode(rootValue);

        const mid = inorderMap.get(rootValue);

        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);

        return root;
    }

    return build(0, inorder.length - 1);
};

