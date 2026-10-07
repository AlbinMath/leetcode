class Solution {
    function sortedArrayToBST($nums) {
        return $this->buildTree($nums, 0, count($nums) - 1);
    }

    function buildTree($nums, $left, $right) {
        // No elements
        if ($left > $right) {
            return null;
        }

        // Choose middle element
        $mid = intdiv($left + $right, 2);

        // Create root
        $root = new TreeNode($nums[$mid]);

        // Build left subtree
        $root->left = $this->buildTree(
            $nums,
            $left,
            $mid - 1
        );

        // Build right subtree
        $root->right = $this->buildTree(
            $nums,
            $mid + 1,
            $right
        );

        return $root;
    }
}
