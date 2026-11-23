
var rightSideView = function(root) {
    if (root === null) {
        return [];
    }

    const result = [];
    const queue = [root];
    let head = 0;

    while (head < queue.length) {
        const levelSize = queue.length - head;

        for (let i = 0; i < levelSize; i++) {
            const node = queue[head++];

            // The last node at this level is visible from the right.
            if (i === levelSize - 1) {
                result.push(node.val);
            }

            if (node.left !== null) {
                queue.push(node.left);
            }

            if (node.right !== null) {
                queue.push(node.right);
            }
        }
    }

    return result;
};

