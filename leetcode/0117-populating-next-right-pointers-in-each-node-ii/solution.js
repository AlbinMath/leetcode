
var connect = function(root) {
    if (root === null) return null;

    let current = root;

    while (current !== null) {
        // Dummy node for building the next level
        const dummy = new Node(0);
        let tail = dummy;

        // Traverse the current level
        while (current !== null) {
            if (current.left !== null) {
                tail.next = current.left;
                tail = tail.next;
            }

            if (current.right !== null) {
                tail.next = current.right;
                tail = tail.next;
            }

            current = current.next;
        }

        // Move to the first node of the next level
        current = dummy.next;
    }

    return root;
};

