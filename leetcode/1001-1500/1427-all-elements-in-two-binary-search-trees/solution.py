class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode, res: List[int]):
            if not node:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
            
        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)
        
        # Merge two sorted lists
        merged = []
        i, j = 0, 0
        len1, len2 = len(list1), len(list2)
        
        while i < len1 and j < len2:
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
                
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged
