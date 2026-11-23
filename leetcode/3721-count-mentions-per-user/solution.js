var countMentions = function(numberOfUsers, events) {
    events.sort((a, b) => {
        const tsDiff = Number(a[1]) - Number(b[1]);
        if (tsDiff !== 0) return tsDiff;
        return a[0] === "OFFLINE" ? -1 : 1;
    });

    const mentions = new Array(numberOfUsers).fill(0);
    const onlineAt = new Array(numberOfUsers).fill(0);

    for (const [type, tsStr, payload] of events) {
        const ts = Number(tsStr);
        if (type === "OFFLINE") {
            onlineAt[Number(payload)] = ts + 60;
        } else if (payload === "ALL") {
            for (let u = 0; u < numberOfUsers; u++) {
                mentions[u]++;
            }
        } else if (payload === "HERE") {
            for (let u = 0; u < numberOfUsers; u++) {
                if (onlineAt[u] <= ts) {
                    mentions[u]++;
                }
            }
        } else {
            for (const token of payload.split(" ")) {
                const u = Number(token.slice(2));
                mentions[u]++;
            }
        }
    }

    return mentions;
};
