var taskSchedulerII = function(tasks, space) {
    const nextAvailable = new Map();
    let days = 0;

    for (const task of tasks) {
        days++;
        if (nextAvailable.has(task) && days < nextAvailable.get(task)) {
            days = nextAvailable.get(task);
        }

        // 'space' full days must pass after 'days' before repeating this task
        nextAvailable.set(task, days + space + 1);
    }

    return days;
};
