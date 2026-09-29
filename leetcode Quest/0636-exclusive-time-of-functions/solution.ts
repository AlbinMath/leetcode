function exclusiveTime(n: number, logs: string[]): number[] {
    const result = new Array(n).fill(0);
    const stack: number[] = [];

    let prevTime = 0;

    for (const log of logs) {
        const [idStr, type, timeStr] = log.split(":");
        const id = Number(idStr);
        const time = Number(timeStr);

        if (type === "start") {
            // Previous function runs until just before this start
            if (stack.length > 0) {
                result[stack[stack.length - 1]] += time - prevTime;
            }

            stack.push(id);
            prevTime = time;
        } else {
            // Current function runs through the end timestamp
            result[stack.pop()!] += time - prevTime + 1;

            // Next execution starts after this timestamp
            prevTime = time + 1;
        }
    }

    return result;
}
