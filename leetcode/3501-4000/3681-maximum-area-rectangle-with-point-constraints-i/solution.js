
var maxRectangleArea = function(points) {
    const pointSet = new Set(
        points.map(([x, y]) => `${x},${y}`)
    );

    let maxArea = -1;
    const n = points.length;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const [x1, y1] = points[i];
            const [x2, y2] = points[j];

            if (x1 === x2 || y1 === y2) continue;

            const left = Math.min(x1, x2);
            const right = Math.max(x1, x2);
            const bottom = Math.min(y1, y2);
            const top = Math.max(y1, y2);

            const corners = [
                `${left},${bottom}`,
                `${left},${top}`,
                `${right},${bottom}`,
                `${right},${top}`
            ];

            if (!corners.every(corner => pointSet.has(corner))) {
                continue;
            }

            let valid = true;

            for (let k = 0; k < n; k++) {
                const [x, y] = points[k];

                // Skip all four rectangle corners.
                if (corners.includes(`${x},${y}`)) continue;

                // Any other point inside or on the border invalidates it.
                if (
                    x >= left && x <= right &&
                    y >= bottom && y <= top
                ) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                const area = (right - left) * (top - bottom);
                maxArea = Math.max(maxArea, area);
            }
        }
    }

    return maxArea;
};

