
var sortedArrayToBST = function(nums) {
    function buildTree(left, right) {
        if (left > right) {
            return null;
        }

        // Choose the middle element as the root.
        const mid = Math.floor((left + right) / 2);
        const root = new TreeNode(nums[mid]);

        // Build the left and right subtrees.
        root.left = buildTree(left, mid - 1);
        root.right = buildTree(mid + 1, right);

        return root;
    }

    return buildTree(0, nums.length - 1);
};

