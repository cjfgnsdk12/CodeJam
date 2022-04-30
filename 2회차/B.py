import math

T=int(input())

for _ in range(T):
    n, m=list(map(int,input().split()))
    A=list(map(int,input().split()))
    m_list=[]
    for _ in range(m):
        m_list.append(list(map(int,input().split())))

    count_position=[0]*(len(A))

    for x,y in m_list: # 10^5
        for i in range(x,y+1): # 10^8
            count_position[i-1]=count_position[i-1]+1
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
