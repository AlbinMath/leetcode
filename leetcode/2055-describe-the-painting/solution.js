var splitPainting = function(segments) {
    let events = new Map();
    for (let [start, end, color] of segments) {
        events.set(start, (events.get(start) || 0) + color);
        events.set(end, (events.get(end) || 0) - color);
    }
    let positions = [...events.keys()].sort((a, b) => a - b);

    let result = [];
    let currentSum = 0;
    for (let i = 0; i < positions.length - 1; i++) {
        let start = positions[i];
        let end = positions[i + 1];
        currentSum += events.get(start);
        if (currentSum > 0) {
            result.push([start, end, currentSum]);
        }
    }

    return result;
};

