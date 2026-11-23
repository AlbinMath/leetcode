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
    function invertTree($root) {
        // Empty tree
        if ($root === null) {
            return null;
        }

        // Swap left and right
        $temp = $root->left;
        $root->left = $root->right;
        $root->right = $temp;

        // Invert subtrees
        $this->invertTree($root->left);
        $this->invertTree($root->right);

        return $root;
    }
}
