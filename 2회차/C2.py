
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

    # max_v_key=max(v_dict, key=v_dict.get)
    max_v_key=[k for k,val in v_dict.items() if max(v_dict.values()) == val]
    max_v_key=max_v_key[-1]
    max_v=v_dict[max_v_key]
    sum_v=sum(v_dict.values())
    loss=sum_v-max_v
    result_arr=[]

    pointer=1
    previous_pointer=-1
    
    if max_v>(loss+1):
        print('IMPOSSIBLE')
        continue
    else:
        for _ in range(m):
            if max_v==loss+1:# 최대값이 나머지랑 같으면
                
                if previous_pointer == max_v_key:# 이전값과 같다면
                    loss-=1
                    tmp_pointer=max_v_key+1
                    # 0이면 패스
                    while v_dict[tmp_pointer]==0:
                        tmp_pointer+=1
                    if tmp_pointer==previous_pointer:
                       tmp_pointer+=1 
                    result_arr.append(tmp_pointer)
                    v_dict[tmp_pointer]-=1  # 넣은부분 빼기
                    previous_pointer=tmp_pointer
                
                else:
                    max_v-=1
                    result_arr.append(max_v_key)
                    v_dict[max_v_key]-=1
                    previous_pointer=max_v_key
                
            else: # 나머지가 최대값보다 크면
                # 포인터가 0이면 증가
                
                while v_dict[pointer]==0:
                    pointer+=1
                # 직전에 봤으면 다음꺼
                if previous_pointer == pointer:
                    next_pointer=pointer+1
                    # 0이면 패스
                    while v_dict[next_pointer]==0:
                        next_pointer+=1
                    if next_pointer==previous_pointer:
                       next_pointer+=1 
                    result_arr.append(next_pointer)
                    if next_pointer==max_v_key:
                        max_v-=1
                    else:
                        loss-=1
                    v_dict[next_pointer]-=1  # 넣은부분 빼기
                    previous_pointer=next_pointer
                else: # 직전이 포인터랑 다르면
                    result_arr.append(pointer)
                    if pointer==max_v_key:
                        max_v-=1
                    else:
                        loss-=1
                    v_dict[pointer]-=1
                    previous_pointer=pointer
    print(result_arr)
    
