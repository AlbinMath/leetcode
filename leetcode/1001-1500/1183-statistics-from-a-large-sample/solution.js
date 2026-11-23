var sampleStats = function(count) {
    let min = -1;
    let max = -1;
    let sum = 0;
    let total = 0;
    let mode = 0;
    let maxFreq = 0;

    for (let i = 0; i < 256; i++) {
        if (count[i] > 0) {
            if (min === -1) min = i;
            max = i;

            sum += i * count[i];
            total += count[i];

            if (count[i] > maxFreq) {
                maxFreq = count[i];
                mode = i;
            }
        }
    }

    const mean = sum / total;

    let median1 = -1;
    let median2 = -1;
    let cumulative = 0;

    for (let i = 0; i < 256; i++) {
        cumulative += count[i];

        if (median1 === -1 && cumulative >= Math.floor((total + 1) / 2)) {
            median1 = i;
        }

        if (cumulative >= Math.floor(total / 2) + 1) {
            median2 = i;
            break;
        }
    }

    const median = (median1 + median2) / 2;

    return [min, max, mean, median, mode];
};
