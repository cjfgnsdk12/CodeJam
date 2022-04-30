import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


from copy import deepcopy

T=int(input())

def possible(tmp_dict):
    max_v_key=max(tmp_dict, key=tmp_dict.get)
    max_v=tmp_dict[max_v_key]
    sum_v=sum(tmp_dict.values())

    if max_v>(sum_v-max_v+1):
        # print('IMPOSSIBLE')
        return False
    else:
        return True

def make_result(arr):
    result=0
    for idx, num in enumerate(arr):
        result+=(idx+1)*num
        result=result%987654323
    return result


def backTracking(depth,previous_key,current_dict, current_candidate):
    # 끝까지 왔으면 스탑
    if result_candi:
        return
    if depth == m:
        result_candi.append(current_candidate)
        return
    
    
    # 현재 상태 점검후 안되면 후보삭제
    if possible(current_dict)==False:
        return
    
    for key in current_dict:
        if key==previous_key:
            continue
        if current_dict[key]==0:
            continue

        next_dict=deepcopy(current_dict)
        next_candidate=deepcopy(current_candidate)
        # 카운트 빼기
        next_dict[key]-=1
        next_candidate.append(key)
        next_depth=depth
        next_depth+=1
        backTracking(next_depth,key,next_dict,next_candidate)
    



for _ in range(T):
    n=int(input())
    v=[0]
    tmp=list(map(int,input().split()))
    v=v+tmp

    m=0
    v_dict={}
    for idx, v_num in enumerate(v):
        if idx==0:
            continue
        v_dict[idx]=v_num
        m+=v_num

    if possible(v_dict)==False:
        print('IMPOSSIBLE')
        continue
    else:
        result_candi=[]
        backTracking(0,0,v_dict,[])
        result_candi.sort()
        print(make_result(result_candi[0]))
    
