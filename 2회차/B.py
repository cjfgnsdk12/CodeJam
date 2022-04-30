import math

T=int(input())

for _ in range(T):
    n, m=list(map(int,input().split()))
    A=list(map(int,input().split()))
    st_list=[]
    end_list=[]
    for _ in range(m):
        tmp=list(map(int,input().split()))
        st_list.append(tmp[0])
        end_list.append(tmp[1])

    count_position=[0]*(len(A))

    st_list.sort()
    end_list.sort()

    st_pos=[0]*(len(A))
    end_pos=[0]*(len(A))
    
    for st in st_list:
        st_pos[st-1]+=1
    for end in end_list:
        end_pos[end-1]+=1
    
    stack=0
    for i in range(len(A)):
        if st_pos[i]>0:
            stack+=st_pos[i]
            count_position[i]=stack
        else:
            count_position[i]=stack
        if end_pos[i]>0:
            stack-=end_pos[i]

    count_position.sort(reverse=True)
    A.sort(reverse=True)
    result_sum=0
    dict={}
    for idx, num in enumerate(count_position):
        result_sum+=num*A[idx]
        if num in dict:
            dict[num]+=1
        else:
            dict[num]=1
    result_cnt=1
    for i in list(dict.values()):
        if i>1:
            result_cnt*= math.factorial(i)

    result_cnt=result_cnt%1000000007

    print(result_sum, result_cnt)
