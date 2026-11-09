
var crackSafe = function(n, k) {
    let visited = new Set();
    let result = [];

    let start = "0".repeat(n - 1);

    function dfs(node) {
        for (let i = 0; i < k; i++) {
            let edge = node + i;

            if (!visited.has(edge)) {
                visited.add(edge);

                dfs(edge.slice(1));

                result.push(i);
            }
        }
    }

    dfs(start);

    // Reverse the postorder result
    result.reverse();

    return start + result.join("");
};

