
var maximumGap = function(skill, station) {
    const n = skill.length;
    const m = station.length;

    const earliest = new Array(n);
    const latest = new Array(n);

    let j = 0;

    for (let i = 0; i < n; i++) {
        while (station[j] !== skill[i]) {
            j++;
        }

        earliest[i] = j;
        j++;
    }

    j = m - 1;

    for (let i = n - 1; i >= 0; i--) {
        while (station[j] !== skill[i]) {
            j--;
        }

        latest[i] = j;
        j--;
    }

    let answer = 0;

    for (let i = 1; i < n; i++) {
        answer = Math.max(
            answer,
            latest[i] - earliest[i - 1]
        );
    }

    return answer;
};

