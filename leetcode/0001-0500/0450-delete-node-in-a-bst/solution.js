
var deleteNode = function(root, key) {
    if (root === null) {
        return null;
    }

    if (key < root.val) {
        root.left = deleteNode(root.left, key);
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key);
    } else {
        // Case 1: No left child
        if (root.left === null) {
            return root.right;
        }

        // Case 2: No right child
        if (root.right === null) {
            return root.left;
        }

        // Case 3: Two children
        let successor = root.right;

        while (successor.left !== null) {
            successor = successor.left;
        }

        root.val = successor.val;
        root.right = deleteNode(root.right, successor.val);
    }

    return root;
};

