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
    function preorderTraversal($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $stack = [$root];

        while (!empty($stack)) {
            // Take the top node
            $node = array_pop($stack);

            // Visit root
            $result[] = $node->val;

            // Push right first
            if ($node->right !== null) {
                $stack[] = $node->right;
            }

            // Push left second
            if ($node->left !== null) {
                $stack[] = $node->left;
            }
        }

        return $result;
    }
}
