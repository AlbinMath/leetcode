from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return ""
        out = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                out.append("#")
            else:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(out)

    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root
