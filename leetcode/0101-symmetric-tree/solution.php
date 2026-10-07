class Solution {
    function isSymmetric($root) {
        return $this->isMirror($root->left, $root->right);
    }

    function isMirror($left, $right) {

        // Both are empty
        if ($left === null && $right === null) {
            return true;
        }

        // One is empty
        if ($left === null || $right === null) {
            return false;
        }

        // Values are different
        if ($left->val != $right->val) {
            return false;
        }

        // Compare opposite sides
        return $this->isMirror($left->left, $right->right)
            && $this->isMirror($left->right, $right->left);
    }
}
