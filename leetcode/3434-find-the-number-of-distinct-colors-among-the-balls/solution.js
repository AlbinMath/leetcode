var queryResults = function(limit, queries) {
    const ballColor = new Map();
    const colorCount = new Map();
    const result = new Array(queries.length);

    for (let i = 0; i < queries.length; i++) {
        const [ball, color] = queries[i];

        if (ballColor.has(ball)) {
            const oldColor = ballColor.get(ball);
            const updatedCount = colorCount.get(oldColor) - 1;
            if (updatedCount === 0) {
                colorCount.delete(oldColor);
            } else {
                colorCount.set(oldColor, updatedCount);
            }
        }

        ballColor.set(ball, color);
        colorCount.set(color, (colorCount.get(color) || 0) + 1);
        result[i] = colorCount.size;
    }

    return result;
};
