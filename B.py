'''
1. 그래프 작성
 - 에라스토테네스의 체처럼
 0000과 간선가지는 애들 먼저 찾기 -> 숫자를 아래로는 비교할 필요 없음
  -> 비교하면서 
 - 0001, 0010, 0100, 1000


2. 모든 최단경로 탐색
3. 사전순 -> 이분탐색 확인

-----------------------------------------------------------------------------
푸는 방법이 틀렸음

이문제는 그래프가 아니라
커졋가는 숫자를 사전적으로 찾는 문제임

008 -> 258

첫자리 0 - 1 - 2
둘째자리 0 1 2 3 4 5
총 7번나오는걸 사전순으로 정리하기!


'''

from itertools import product
from collections import deque
import math
import copy
import heapq


# 2개의 노드가 한곳만 다르며 차이가 1인지 체크
def is_diff_one(n1,n2,L):
    diff_cnt=0
    diff_line=0
    ans=False
    for i in range(L):
        if n1[i]!=n2[i]:
            diff_cnt+=1
            diff_line=i
    if diff_cnt==1:
        if abs(int(n1[diff_line])-int(n2[diff_line]))==1:
            ans=True
    return ans

# 속도 개선 필요
def make_graph(node_list):
    graph={}
    for node in node_list:
        graph[node]=[]

    for idx, node in enumerate(node_list):
        for j in range(idx+1, len(node_list)):
            if is_diff_one(node_list[j],node,L):
                graph[node].append(node_list[j])
                graph[node_list[j]].append(node)
    return graph

# 2번쨰
def make_graph_second(node_list):
    graph={}
    for node in node_list:
        graph[node]=[]

    for node in node_list:
        for i in range(L):
            tmp_node=node
            if int(tmp_node[i])==9:
                continue
            tmp=list(tmp_node)
            tmp[i]=str(int(tmp_node[i])+1)
            tmp_node="".join(tmp)
            graph[node].append(tmp_node)
            graph[tmp_node].append(node)



    return graph

# 숫자를 문자열로 5 ->'05'
def int_to_str(n):
    n=str(n)
    if len(n)<L:
        n='0'*(L-len(n))+n
    return n

# bfs
def bfs(graph,start, destination):
    ans=[]
    dist=int(math.pow(10,19))
    visited_len =int(math.pow(10,L))
    visited={}
    for i in range(visited_len):
        i=int_to_str(i)
        visited[i]=dist

    queue=[[start]]
    visited[start] = 1
    
    while queue:
        path=queue.pop(0)
        print(path)
        if len(path)>dist:
            break
        V=path[-1]
        if V==destination:
            dist=len(path)
            ans.append(path)
        for w in graph[V]:
            if visited[V]>visited[w]:
                continue
            visited[w] = len(path)+1
            new_path=copy.deepcopy(path)
            new_path.append(w)
            queue.append(new_path)
    return ans


# 다익스트라 알고리즘

def dijkstra(graph, start,destination):
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], [start]])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, path = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
        current_destination=path[-1]
        

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue    
        
        for new_destination in graph[current_destination]:
            distance = current_distance + 1  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                new_path=copy.deepcopy(path)
                new_path.append(new_destination)
                heapq.heappush(queue, [distance, new_path])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        
    return distances    




T=int(input())
for _ in range(T):
    L,K,x,y=input().split()
    L=int(L)
    K=int(K)
    node_list=[]
    graph={}
    # node 생성
    for node_ in product(['0','1','2','3','4','5','6','7','8','9'], repeat=L):
        tmp_node=''
        for i in range(len(node_)):
            tmp_node=tmp_node+node_[i]
        node_list.append(tmp_node)
    graph=make_graph_second(node_list)
    ans=bfs(graph,x,y)

    if len(ans)>=K:
        print(' '.join(ans[K-1]))
    else:
        print('NO')
