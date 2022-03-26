T=int(input())

for _ in range(T):
    n,L,F=map(int,input().split())
    W=input().split()
    last_word={}
    for w in W:
        if w[-F:] in last_word:
            last_word[w[-F:]]+=1
        else:
            last_word[w[-F:]]=1
        ans=0   
        for l_word in last_word:
            if last_word[l_word]>=2:
                ans=ans+last_word[l_word]//2
    print(ans)
    
