
var generateTrees = function(n) {
    function build(start, end) {
        const trees = [];

        // Empty subtree
        if (start > end) {
            return [null];
        }

        for (let rootVal = start; rootVal <= end; rootVal++) {
            const leftTrees = build(start, rootVal - 1);
            const rightTrees = build(rootVal + 1, end);

            // Combine every left and right subtree
            for (const left of leftTrees) {
                for (const right of rightTrees) {
                    const root = new TreeNode(rootVal);
                    root.left = left;
                    root.right = right;
                    trees.push(root);
                }
            }
        }

        return trees;
    }

    return build(1, n);
};

