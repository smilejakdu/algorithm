graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


def recursive_dfs(v, discovered=[]):
    print(v)
    discovered.append(v)            # 해당 노드 방문 체크
    for w in graph[v]:              # 해당 노드에 연결된 노드를 순회
        if w not in discovered:     # 방문하지 않은 노드라면
            discovered = recursive_dfs(w, discovered)
    return discovered
# print(recursive_dfs(5))


def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(iterative_dfs(1))