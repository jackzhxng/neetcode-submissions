import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Time taken: 20 min
        """
        adj = [[] for _ in range(n + 1)]
        for u, v, dist in times:
            adj[u].append((v, dist))

        pq = []
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        heapq.heappush(pq, (0, k))

        while pq:
            u_distance, u = heapq.heappop(pq)
            if u_distance > distances[u]: # Lots of algos online do !=, but technically this will never be < since the distance is always updated if it is smaller before it is thrown onto the heap. So if that is the case it will always just be =.
                continue
            for v, v_distance in adj[u]:
                if u_distance + v_distance < distances[v]:
                    distances[v] = u_distance + v_distance
                    heapq.heappush(pq, (distances[v], v))
        
        max_dist = max(distances[1:])
        return -1 if max_dist == float("inf") else max_dist