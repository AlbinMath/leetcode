var leafSimilar = function(root1, root2) {
    function getLeaves(root, leaves) {
        if (root === null) {
            return;
        }

        if (root.left === null && root.right === null) {
            leaves.push(root.val);
            return;
        }

        getLeaves(root.left, leaves);
        getLeaves(root.right, leaves);
    }

    const leaves1 = [];
    const leaves2 = [];

    getLeaves(root1, leaves1);
    getLeaves(root2, leaves2);

    if (leaves1.length !== leaves2.length) {
        return false;
    }

    for (let i = 0; i < leaves1.length; i++) {
        if (leaves1[i] !== leaves2[i]) {
            return false;
        }
    }

    return true;
};
