/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = 0;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */

class Solution {
    function postorderTraversal($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $stack = [$root];

        while (!empty($stack)) {
            $node = array_pop($stack);

            // Add root first
            $result[] = $node->val;

            // Push left first
            if ($node->left !== null) {
                $stack[] = $node->left;
            }

            // Push right second
            if ($node->right !== null) {
                $stack[] = $node->right;
            }
        }

        // Root → Right → Left
        // Reverse → Left → Right → Root
        return array_reverse($result);
    }
}
