'''
1. 그래프 작성
 - 에라스토테네스의 체처럼
 0000과 간선가지는 애들 먼저 찾기 -> 숫자를 아래로는 비교할 필요 없음
  -> 비교하면서 
 - 0001, 0010, 0100, 1000


2. 모든 최단경로 탐색
3. 사전순 -> 이분탐색 확인

'''

from itertools import product


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
        if abs(int(n1[diff_line])-int(n2[diff_line])):
            ans=True
    return ans

# 속도 개선 필요
def make_graph(node_list):
    graph={}
    
    

    return graph

T=int(input())

for _ in range(T):
    L,K,x,y=map(int,input().split())
    node_list=[]
    graph={}
    # node 생성
    for node_ in product(['0','1','2','3','4','5','6','7','8','9'], repeat=2):
        node_list.append(node_[0]+node_[1])
    print(node_list)





