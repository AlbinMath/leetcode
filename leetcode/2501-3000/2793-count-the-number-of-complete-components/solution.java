import java.util.*;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        List<Integer>[] graph = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }

            int vertices = 0;
            int edgeCount = 0;

            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            visited[i] = true;

            while (!queue.isEmpty()) {
                int node = queue.poll();
                vertices++;
                edgeCount += graph[node].size();

                for (int next : graph[node]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.offer(next);
                    }
                }
            }

            // Every pair of vertices must have an edge.
            // A complete graph with k vertices has k*(k-1)/2 edges.
            edgeCount /= 2;

            if (edgeCount == vertices * (vertices - 1) / 2) {
                answer++;
            }
        }

        return answer;
    }
}
