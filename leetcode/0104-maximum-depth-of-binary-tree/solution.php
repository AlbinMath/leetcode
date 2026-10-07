class Solution {
    function maxDepth($root) {
        // Empty tree
        if ($root === null) {
            return 0;
        }

        // Calculate left and right depths
        $leftDepth = $this->maxDepth($root->left);
        $rightDepth = $this->maxDepth($root->right);

        // Current node + deeper subtree
        return 1 + max($leftDepth, $rightDepth);
    }
}
