
var minEnergy = function(n, brightness, intervals) {
    const bulbsNeeded = Math.ceil(brightness / 3);

    intervals.sort((a, b) => a[0] - b[0]);

    let totalTime = 0;

    let start = intervals[0][0];
    let end = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        const [nextStart, nextEnd] = intervals[i];

        if (nextStart <= end + 1) {
            end = Math.max(end, nextEnd);
        } else {
            totalTime += end - start + 1;

            start = nextStart;
            end = nextEnd;
        }
    }

    totalTime += end - start + 1;

    return totalTime * bulbsNeeded;
};

