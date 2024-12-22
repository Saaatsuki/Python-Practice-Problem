import sys
sys.setrecursionlimit(2000)

def dfs(node, parent):
    # 현재 노드가 특별 노드가 아니었을 때, 자식들의 정보에서 최소값을 계산
    dp[node][0] = sum(min(dp[child][0], dp[child][1]) for child in tree[node] if child != parent)
    
    # 현재 노드가 특별 노드일 경우, 자식들의 정보에서 최소값을 계산
    dp[node][1] = node_weights[node] + sum(dp[child][0] for child in tree[node] if child != parent)

    # 자식 노드들에 대해서 dfs 호출
    for child in tree[node]:
        if child != parent:
            dfs(child, node)

# 입력 받기
n, root = map(int, input().split())
node_weights = [0] + list(map(int, input().split()))  # 노드 번호가 1부터 시작하므로 0번 인덱스는 비워둠
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# dp 배열 초기화
dp = [[0, 0] for _ in range(n + 1)]  # dp[u][0]: u가 특별 노드가 아닐 때, dp[u][1]: u가 특별 노드일 때

# 루트에서부터 DFS 시작
dfs(root, -1)

# 최소 가중치 합 출력
print(min(dp[root][0], dp[root][1]))
