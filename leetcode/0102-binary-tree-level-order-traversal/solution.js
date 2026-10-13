var levelOrder = function(root) {
    if (root === null) return [];

    const result = [];
    const queue = [root];
    let front = 0;

    while (front < queue.length) {
        const levelSize = queue.length - front;
        const level = [];

        for (let i = 0; i < levelSize; i++) {
            const node = queue[front++];
            level.push(node.val);

            if (node.left !== null) {
                queue.push(node.left);
            }

            if (node.right !== null) {
                queue.push(node.right);
            }
        }

        result.push(level);
    }

    return result;
};
