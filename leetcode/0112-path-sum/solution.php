class Solution {
    function hasPathSum($root, $targetSum) {
        if ($root === null) {
            return false;
        }

        // Leaf node
        if ($root->left === null && $root->right === null) {
            return $root->val == $targetSum;
        }

        $remaining = $targetSum - $root->val;

        return $this->hasPathSum($root->left, $remaining)
            || $this->hasPathSum($root->right, $remaining);
    }
}
