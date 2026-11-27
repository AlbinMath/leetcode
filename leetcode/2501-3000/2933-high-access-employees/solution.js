
var findHighAccessEmployees = function(access_times) {
    const map = new Map();
    const result = [];
    for (const [name, time] of access_times) {
        const hours = Number(time.slice(0, 2));
        const minutes = Number(time.slice(2, 4));

        const totalMinutes = hours * 60 + minutes;

        if (!map.has(name)) {
            map.set(name, []);
        }
        map.get(name).push(totalMinutes);
    }
    for (const [name, times] of map) {
        times.sort((a, b) => a - b);

        for (let i = 0; i + 2 < times.length; i++) {
            if (times[i + 2] - times[i] < 60) {
                result.push(name);
                break;
            }
        }
    }
    return result;
};

