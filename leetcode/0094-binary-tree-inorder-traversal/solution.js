
var inorderTraversal = function(root) {
    const result = [];
    const stack = [];
    let current = root;

    while (current !== null || stack.length > 0) {
        // Go as far left as possible
        while (current !== null) {
            stack.push(current);
            current = current.left;
        }

        // Visit the node
        current = stack.pop();
        result.push(current.val);

        // Explore the right subtree
        current = current.right;
    }

    return result;
};

