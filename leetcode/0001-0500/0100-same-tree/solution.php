class Solution {
    function isSameTree($p, $q) {

        // Both nodes are empty
        if ($p === null && $q === null) {
            return true;
        }

        // One is empty, the other is not
        if ($p === null || $q === null) {
            return false;
        }

        // Values are different
        if ($p->val != $q->val) {
            return false;
        }

        // Check left and right subtrees
        return $this->isSameTree($p->left, $q->left)
            && $this->isSameTree($p->right, $q->right);
    }
}
