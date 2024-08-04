def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    
    count = 0
    while queue:
        course = queue.popleft()
        count += 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == numCourses

# Example Usage
print(can_finish(2, [[1, 0]]))  # Output: True
print(can_finish(2, [[1, 0], [0, 1]]))  # Output: False
