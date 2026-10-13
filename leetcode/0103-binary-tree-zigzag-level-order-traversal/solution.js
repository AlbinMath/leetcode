
var zigzagLevelOrder = function(root) {
    if (root === null) return [];

    const result = [];
    const queue = [root];
    let front = 0;
    let leftToRight = true;

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

        if (!leftToRight) {
            level.reverse();
        }

        result.push(level);
        leftToRight = !leftToRight;
    }

    return result;
};

