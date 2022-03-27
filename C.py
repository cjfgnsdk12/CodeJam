
import copy


# 각 수를 소인수분해하고 리스트에 넣는 함수
def factorization(x):
    ans=[] 
    d = 2 
    while d**2 <= x: 
        while x%d==0:
            ans.append(d)
            x = x // d 
        d = d + 1
    if x>1:
        ans.append(x)
    
    if ans==[]:
        ans=[1]
    return ans

def factorization_third(x):
    ans=[] 
    d = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 
    97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
    197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
    313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 
    439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
    571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 
    691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 
    829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 
    977, 983, 991, 997]
    n = 0
    while d[n]**2 <= x: 
        while x%d[n]==0:
            ans.append(d[n])
            x = x // d[n]
        n = n + 1
        if n==len(d):
            break
    if x>1:
        ans.append(x)
    
    if ans==[]:
        ans=[1]
    ans.sort()
    return ans



# 두 수의 거리를 비교해주는 함수, 확인필요
def dist(a,b):
    x=hash_fac[a]
    y=hash_fac[b]
    a=copy.deepcopy(x)
    a.reverse()
    b=copy.deepcopy(y)
    b.reverse()
    
    small_length=0
    ans=0
    ans=sum(a)+sum(b)

    if len(a)<+len(b):
        small_length=len(a)
    else:
        small_length=len(b)

    for i in range(small_length):
        if a[i]==b[i]:
            ans=ans- 2*a[i]
        else:
            break
    return ans


# 전체 수를 중복 제거한 후 hash함수에 담기
def make_hash(k):
    hash={}
    length=len(k)
    for i in range(length):
        for j in range(i,length):
            if k[i]==k[j]:
                key=str(k[i])+','+str(k[j])
                hash[key]=0
                continue
            key=str(k[i])+','+str(k[j])
            hash[key]=dist(k[i],k[j])
    return hash

# 행렬의 행 합 만들기
def make_mat(hash,v):
    ans=[]

    for a in v:
        tmp=0
        for b in v:
            if a<=b:
                key=str(a)+','+str(b)
            else:
                key=str(b)+','+str(a)
            tmp=tmp+hash[key]
        ans.append(tmp)
    return ans




def make_fac_hash(k):
    hash_fac={}
    for k_ in k:
        hash_fac[k_]=factorization_third(k_)
    return hash_fac

# print(factorization_second(42))
# exit()

def eratosthenes(n):
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False                
    return [ i for i in range(2,n) if sieve[i] == True]

# print(dist(20,24))
# exit()



T=int(input())

for _ in range(T):
    n=int(input())
    v=list(map(int,input().split()))

    # k는 중복제거 후 정렬
    k=set(v) 
    k=list(k)
    k.sort()

    hash_fac=make_fac_hash(k)
    hash=make_hash(k)
    # print(hash)
    v.sort()
    mat=make_mat(hash,v)
    # print(mat)
    print((sum(mat)-2*max(mat))//2)


    
