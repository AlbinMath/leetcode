
var maxAmount = function(initialCurrency, pairs1, rates1, pairs2, rates2) {
    function buildGraph(pairs, rates) {
        const graph = new Map();

        function addEdge(from, to, rate) {
            if (!graph.has(from)) {
                graph.set(from, []);
            }
            graph.get(from).push([to, rate]);
        }

        for (let i = 0; i < pairs.length; i++) {
            const [from, to] = pairs[i];
            const rate = rates[i];

            addEdge(from, to, rate);
            addEdge(to, from, 1 / rate);
        }

        return graph;
    }

    function calculateRates(graph, start) {
        const amounts = new Map();
        amounts.set(start, 1.0);

        const stack = [start];

        while (stack.length > 0) {
            const currency = stack.pop();
            const amount = amounts.get(currency);

            for (const [next, rate] of graph.get(currency) || []) {
                if (amounts.has(next)) continue;

                amounts.set(next, amount * rate);
                stack.push(next);
            }
        }

        return amounts;
    }

    const graph1 = buildGraph(pairs1, rates1);
    const graph2 = buildGraph(pairs2, rates2);

    // Day 1: Currency obtainable from 1 initial currency.
    const day1 = calculateRates(graph1, initialCurrency);

    // Day 2: Currency obtainable from 1 initial currency.
    const day2 = calculateRates(graph2, initialCurrency);

    let answer = 1.0;

    for (const [currency, amountDay1] of day1) {
        if (day2.has(currency)) {
            // Reverse the Day 2 conversion rate.
            const amountDay2 = 1 / day2.get(currency);

            answer = Math.max(
                answer,
                amountDay1 * amountDay2
            );
        }
    }

    return answer;
};

