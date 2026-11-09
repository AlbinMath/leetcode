
var edgeScore = function(edges) {
    const n = edges.length;

    // Store the edge score of each node
    const score = new Array(n).fill(0);

    // Calculate edge scores
    for (let i = 0; i < n; i++) {
        score[edges[i]] += i;
    }

    let maxScore = -1;
    let answer = 0;

    // Find the node with the highest score
    for (let i = 0; i < n; i++) {
        if (score[i] > maxScore) {
            maxScore = score[i];
            answer = i;
        }
    }

    return answer;
};

