var minProcessingTime = function(processorTime, tasks) {
    processorTime.sort((a, b) => a - b);
    tasks.sort((a, b) => b - a);

    let ans = 0;

    for (let i = 0; i < processorTime.length; i++) {
        let maxTask = tasks[i * 4];

        let time = processorTime[i] + maxTask;

        ans = Math.max(ans, time);
    }

    return ans;
};
