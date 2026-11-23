class Solution {
    function inorderTraversal($root) {
        $result = [];
        $stack = [];
        $current = $root;

        while ($current !== null || !empty($stack)) {

            // Go as far left as possible
            while ($current !== null) {
                $stack[] = $current;
                $current = $current->left;
            }

            // Process the node
            $current = array_pop($stack);
            $result[] = $current->val;

            // Move to the right subtree
            $current = $current->right;
        }

        return $result;
    }
}
