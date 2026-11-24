var maxLevelSum = function(root) {
    const queue = [root];
    let level = 1;
    let maxSum = -Infinity;
    let result = 1;

    while (queue.length > 0) {
        const levelSize = queue.length;
        let sum = 0;

        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            sum += node.val;

            if (node.left !== null) {
                queue.push(node.left);
            }

            if (node.right !== null) {
                queue.push(node.right);
            }
        }

        if (sum > maxSum) {
            maxSum = sum;
            result = level;
        }

        level++;
    }

    return result;
};
