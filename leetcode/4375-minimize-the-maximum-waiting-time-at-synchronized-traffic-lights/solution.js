var minPenalty = function(period, lights, arrivalTime) {
    const maxGreen = Math.max(...lights);

    let answer = 0;

    for (const time of arrivalTime) {
        const r = time % period;

        if (r >= maxGreen) {
            answer = Math.max(answer, period - r);
        }
    }

    return answer;
};
