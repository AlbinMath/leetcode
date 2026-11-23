class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        val_to_tree = {}
        leaf_counts = collections.defaultdict(int)

        # 1. Map root values and count all leaf occurrences
        for tree in trees:
            val_to_tree[tree.val] = tree
            if tree.left:
                leaf_counts[tree.left.val] += 1
            if tree.right:
                leaf_counts[tree.right.val] += 1

        # 2. Find the unique global root candidate
        global_root = None
        for tree in trees:
            if tree.val not in leaf_counts:
                if global_root is not None:
                    return None  # Multiple candidates -> disjoint components
                global_root = tree

        if not global_root:
            return None

        # 3. Merge and validate BST via DFS with range limits (lower, upper)
        def validate_and_merge(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            # If it's a leaf and can be expanded with another tree
            if not node.left and not node.right:
                if node.val in val_to_tree and node != global_root:
                    attached = val_to_tree.pop(node.val)
                    node.left = attached.left
                    node.right = attached.right

            return (validate_and_merge(node.left, lower, node.val) and
                    validate_and_merge(node.right, node.val, upper))

        # Check if BST properties hold during traversal & expansion
        if not validate_and_merge(global_root, float('-inf'), float('inf')):
            return None

        # All trees except the global_root must have been merged and removed
        return global_root if len(val_to_tree) == 1 else None
