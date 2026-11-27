var maxPoints = function(technique1, technique2, k) {
    const n = technique1.length;

    const tasks = [];

    for (let i = 0; i < n; i++) {
        tasks.push({
            diff: technique1[i] - technique2[i],
            a: technique1[i],
            b: technique2[i]
        });
    }

    tasks.sort((a, b) => b.diff - a.diff);

    let total = 0;

    for (let i = 0; i < n; i++) {
        if (i < k || tasks[i].diff > 0) {
            total += tasks[i].a;
        } else {
            total += tasks[i].b;
        }
    }

    return total;
};
