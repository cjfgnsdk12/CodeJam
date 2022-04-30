from itertools import permutations

T=int(input())

for _ in range(T):
    n=int(input())
    Bob=int(input())
    Alice=list(input())
    
    # Bob 뒤집었을 떄 더 작은 숫자
    Bob2=int(str(Bob)[::-1])
    if Bob2<Bob:
        Bob=Bob2
    
    # Alice 조합 구하기
    candi=list(permutations(Alice,n))
    tmp=0
    for can in candi:
        can_int=int(''.join(can))
        if can_int>=Bob:
            continue
        else:
            if tmp<can_int:
                tmp=can_int
    if tmp!=0:
        print(tmp)
    else:
        Alice.sort(reverse=True)
        Alice=Alice[0:-1]
        print(int(''.join(Alice)))

    
