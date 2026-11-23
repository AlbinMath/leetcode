
var recoverTree = function(root) {
    let first = null;
    let second = null;
    let prev = null;
    let curr = root;

    // Morris inorder traversal: O(1) extra space
    while (curr !== null) {
        if (curr.left === null) {
            // Visit current node
            if (prev !== null && prev.val > curr.val) {
                if (first === null) {
                    first = prev;
                }
                second = curr;
            }

            prev = curr;
            curr = curr.right;
        } else {
            // Find inorder predecessor
            let pred = curr.left;

            while (pred.right !== null && pred.right !== curr) {
                pred = pred.right;
            }

            if (pred.right === null) {
                // Create temporary thread
                pred.right = curr;
                curr = curr.left;
            } else {
                // Remove temporary thread
                pred.right = null;

                // Visit current node
                if (prev !== null && prev.val > curr.val) {
                    if (first === null) {
                        first = prev;
                    }
                    second = curr;
                }

                prev = curr;
                curr = curr.right;
            }
        }
    }

    // Restore the two swapped values
    if (first !== null && second !== null) {
        [first.val, second.val] = [second.val, first.val];
    }
};

