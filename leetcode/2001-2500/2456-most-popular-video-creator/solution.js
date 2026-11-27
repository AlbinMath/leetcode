
var mostPopularCreator = function(creators, ids, views) {
    const map = new Map();

    for (let i = 0; i < creators.length; i++) {
        const creator = creators[i];
        const id = ids[i];
        const view = views[i];

        if (!map.has(creator)) {
            map.set(creator, {
                totalViews: 0,
                maxViews: -1,
                bestId: ""
            });
        }

        const data = map.get(creator);

        data.totalViews += view;

        if (
            view > data.maxViews ||
            (view === data.maxViews && id < data.bestId)
        ) {
            data.maxViews = view;
            data.bestId = id;
        }
    }

    let maxPopularity = 0;

    for (const data of map.values()) {
        maxPopularity = Math.max(
            maxPopularity,
            data.totalViews
        );
    }

    const answer = [];

    for (const [creator, data] of map) {
        if (data.totalViews === maxPopularity) {
            answer.push([creator, data.bestId]);
        }
    }

    return answer;
};

