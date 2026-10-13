
var kthSmallest = function(root, k) {
    const stack = [];
    let current = root;
    let count = 0;

    while (current !== null || stack.length > 0) {
        // Traverse as far left as possible
        while (current !== null) {
            stack.push(current);
            current = current.left;
        }

        // Visit the next smallest node
        current = stack.pop();
        count++;

        if (count === k) {
            return current.val;
        }

        // Explore the right subtree
        current = current.right;
    }
};

