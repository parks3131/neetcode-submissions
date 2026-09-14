class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        order = []
        states = [UNVISITED]*numCourses
        graph = defaultdict(list)

        def dfs(node):
            if states[node] == VISITED:
                return True
            elif states[node] == VISITING:
                return False
            else:
                states[node] = VISITING
                for i in graph[node]:
                    if not dfs(i):
                        return False
                states[node] = VISITED
                order.append(node)
                return True            

        for i, j in prerequisites:
            graph[i].append(j)
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order