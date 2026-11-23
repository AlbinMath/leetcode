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
    function binaryTreePaths($root) {
        $result = [];

        $this->dfs($root, "", $result);

        return $result;
    }

    function dfs($node, $path, &$result) {
        if ($node === null) {
            return;
        }

        // Add current node to the path
        if ($path === "") {
            $path = (string)$node->val;
        } else {
            $path .= "->" . $node->val;
        }

        // Leaf node
        if ($node->left === null && $node->right === null) {
            $result[] = $path;
            return;
        }

        // Explore left and right subtrees
        $this->dfs($node->left, $path, $result);
        $this->dfs($node->right, $path, $result);
    }
}
