
var findCircleNum = function(isConnected) {
    const n = isConnected.length;
    const visited = new Array(n).fill(false);
    let provinces = 0;

    function dfs(city) {
        visited[city] = true;

        for (let neighbor = 0; neighbor < n; neighbor++) {
            if (isConnected[city][neighbor] === 1 && !visited[neighbor]) {
                dfs(neighbor);
            }
        }
    }

    for (let city = 0; city < n; city++) {
        if (!visited[city]) {
            dfs(city);
            provinces++;
        }
    }

    return provinces;
};

