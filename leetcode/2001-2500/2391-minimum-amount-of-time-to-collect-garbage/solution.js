var garbageCollection = function(garbage, travel) {
    let n = garbage.length;
    let totalPickup = 0;
    let lastM = 0;
    let lastP = 0;
    let lastG = 0;
    for (let i = 0; i < n; i++) {
        totalPickup += garbage[i].length;
        for (let char of garbage[i]) {
            if (char === 'M') {
                lastM = i;
            } else if (char === 'P') {
                lastP = i;
            } else if (char === 'G') {
                lastG = i;
            }
        }
    }
    let totalTime = totalPickup;
    let travelTime = 0;
    for (let i = 0; i < n - 1; i++) {
        travelTime += travel[i];
        if (i + 1 <= lastM) {
            totalTime += travel[i];
        }
        if (i + 1 <= lastP) {
            totalTime += travel[i];
        }
        if (i + 1 <= lastG) {
            totalTime += travel[i];
        }
    }
    return totalTime;
};

