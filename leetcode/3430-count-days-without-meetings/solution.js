
var countDays = function(days, meetings) {
    meetings.sort((a, b) => a[0] - b[0]);

    let lastDay = 0;
    let freeDays = 0;

    for (const [start, end] of meetings) {

        if (start > lastDay + 1) {
            freeDays += start - lastDay - 1;
        }

        lastDay = Math.max(lastDay, end);
    }

    freeDays += days - lastDay;

    return freeDays;
};

