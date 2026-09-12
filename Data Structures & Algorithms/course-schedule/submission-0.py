class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        UNVISITTED = 0
        VISITING = 1
        VISITED = 2
        
        states = [UNVISITTED]*numCourses

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(state):
            if states[state] == VISITED:
                return True
            elif states[state] == VISITING:
                return False
            else:
                states[state] = VISITING
                for i in graph[state]:
                    if not dfs(i):
                        return False
                states[state] = VISITED
                return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        
        

        



