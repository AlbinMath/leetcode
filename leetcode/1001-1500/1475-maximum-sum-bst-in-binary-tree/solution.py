class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def traverse(node):
            nonlocal max_sum
            if not node:
                # is_bst, min_val, max_val, sum_val
                return True, float('inf'), float('-inf'), 0

            left_is_bst, left_min, left_max, left_sum = traverse(node.left)
            right_is_bst, right_min, right_max, right_sum = traverse(node.right)

            # Check BST condition
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, curr_sum)
                
                curr_min = min(left_min, node.val)
                curr_max = max(right_max, node.val)
                return True, curr_min, curr_max, curr_sum

            # Not a BST
            return False, 0, 0, 0

        traverse(root)
        return max_sum
