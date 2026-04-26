class Solution:
    def exploreComponent(self, adj_list: Dict[int, List[int]], node: int, visited: set[int]) -> None:
        if node in visited:
            return
        visited.add(node)
        for adj_node in adj_list[node]:
            self.exploreComponent(adj_list, adj_node, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Time taken: 7 min
        """
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = set()
        num_connected = 0
        for node in adj_list.keys():
            if node in visited:
                continue
            self.exploreComponent(adj_list, node, visited)
            num_connected += 1
        return num_connected

