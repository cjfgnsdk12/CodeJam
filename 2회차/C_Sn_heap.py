from heapq import heapify,heappush,heappop

# 10 10 10 10 10 예외 확인
# 2개 짜리 확인


T=int(input())

def make_result(arr):
    result=0
    for idx, num in enumerate(arr):
        result+=(idx+1)*num
        result=result%987654323
    return result


# 누적합 구하기
def make_sn(v_list):
    sn=[]
    tmp=0
    for v in v_list:
        tmp+=v
        sn.append(tmp)
    return sn

def is_possible(first,second,sn,heap):
    global max_flag
    front_last=max(first,second)
    back_sum=sn[-1]-sn[front_last]

    if back_sum==0:
        return True,0
        
    if heap[0][1] == v_list[first]+v_list[second] + (back_sum -heap[0][1]) +1:
        # heap[0]이 계속 반복되어야함
        max_flag =True

        max_val=heap[0][1]
        for i in range(max(first,second),len(v_list)):
            if max_val== v_list[i]:
                max_idx=i
        result_arr.append(max_idx)
        v_list[max_idx]-=1

        target=min(first,second)
        return max_idx,target
    else:
        return True,0
    


for _ in range(T):
    n=int(input())
    v=[0]
    tmp=list(map(int,input().split()))
    v_list=v+tmp

    # 누적합 만들기
    sn=make_sn(v_list)

    # 힙 만들기
    heap=[]
    for v in v_list:
        heappush(heap, (-v, v)) 

    # 불가능한 애들 검출
    if (sn[-1] - heap[0][1])+1 < heap[0][1]:
        print('IMPOSSIBLE')
        continue

    first=1
    second=2
    result_arr=[0]

    # 시작에 1,2 가 최대값이면 힙 바꿔줌
    while heap[0][1]==v_list[second] or heap[0][1]==v_list[first]:
        heappop(heap)

    # max 반복조건 flag
    max_flag=False
    max_val=True
    last_target=0
    max_chance=False
    # 2개짜리는 예외로 해야할수도있음, # 마지막 처리도 생각해야함
    while True:
        # 종료 조건
        if len(result_arr)==(sn[-1]+1):
            break

        # first, second 반복되는 구간
        if max_flag==False:
            max_val, last_target=is_possible(first,second,sn,heap)
            if max_val==True:
                # first, second 위치 넘김
                if v_list[first]==0:
                    while v_list[first]==0 or first ==second: # first 값이 0 또는 second랑 같으면 다음으로 넘김
                        first+=1
                    # first가 최대면 뒷구간에서 최대값 구함
                    if heap[0][1]==v_list[first]:
                        heappop(heap)
                if v_list[second]==0:
                    while v_list[second]==0 or first ==second: # second 값이 0 또는 first랑 같으면 다음으로 넘김
                        second+=1
                    # second가 최대면 뒷구간에서 최대값 구함
                    if heap[0][1]==v_list[second]:
                        heappop(heap)    
                # 바뀐순간 예외처리 해야함
                target=min(first,second)
                # 작은값 넣을 순서면
                if target!=result_arr[-1]:
                    pass
                else: # 아니면 큰수로
                    target=max(first,second)
                # 삽입
                result_arr.append(target)
                v_list[target]-=1


        else:
            # 한번 최대값은 위에서 넣었음
            # 이후 반복
            if v_list[last_target]==0:
                while v_list[last_target]==0 or last_target==max_val:
                    last_target+=1
                    if last_target==len(v_list):
                        break
            if max_chance==False:
                result_arr.append(last_target)
                v_list[last_target]-=1
                max_chance=True
            else:
                result_arr.append(max_val)
                v_list[max_val]-=1
                max_chance=False
            
        
    print(result_arr)

    
    

    