class Solution {
    function isBalanced($root) {
        return $this->height($root) != -1;
    }

    function height($node) {
        // Empty tree has height 0
        if ($node === null) {
            return 0;
        }

        // Check left subtree
        $leftHeight = $this->height($node->left);

        if ($leftHeight == -1) {
            return -1;
        }

        // Check right subtree
        $rightHeight = $this->height($node->right);

        if ($rightHeight == -1) {
            return -1;
        }

        // Current node is unbalanced
        if (abs($leftHeight - $rightHeight) > 1) {
            return -1;
        }

        // Return height of current subtree
        return 1 + max($leftHeight, $rightHeight);
    }
}
