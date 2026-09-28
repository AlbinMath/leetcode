import java.util.*;

class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();

        // dist[r][c] = distance to the nearest thief
        int[][] dist = new int[n][n];
        for (int[] row : dist) {
            Arrays.fill(row, -1);
        }

        Queue<int[]> queue = new LinkedList<>();

        // Start BFS from all thieves simultaneously
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid.get(r).get(c) == 1) {
                    dist[r][c] = 0;
                    queue.offer(new int[]{r, c});
                }
            }
        }

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        // Multi-source BFS
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n
                        && dist[nr][nc] == -1) {

                    dist[nr][nc] = dist[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }

        // Maximize the minimum safeness along the path
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[2], a[2])
        );

        boolean[][] visited = new boolean[n][n];

        // {row, col, current safeness}
        pq.offer(new int[]{0, 0, dist[0][0]});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();

            int r = cur[0];
            int c = cur[1];
            int safe = cur[2];

            if (visited[r][c]) {
                continue;
            }

            visited[r][c] = true;

            if (r == n - 1 && c == n - 1) {
                return safe;
            }

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n
                        && !visited[nr][nc]) {

                    int newSafe = Math.min(safe, dist[nr][nc]);

                    pq.offer(new int[]{nr, nc, newSafe});
                }
            }
        }

        return -1;
    }
}
