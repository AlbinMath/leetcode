class Solution:
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None

        if original is target:
            return cloned

        left = self.getTargetCopy(
            original.left, cloned.left, target
        )

        if left is not None:
            return left

        return self.getTargetCopy(
            original.right, cloned.right, target
        )
