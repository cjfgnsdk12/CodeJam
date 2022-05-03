import heapq

T = int(input())
for _ in range(T):
    n = int(input())
    v = list(map(int, input().split()))
    m = sum(v)
    index, idx = 0, 1  # index 는 숫자가 가장 작은 사탕, idx 는 그 다음 사탕

    heap = []  # 개수를 최대힙으로 구현
    for i in range(n):
        heapq.heappush(heap, (-v[i], i))

    answer = [-1]
    while m > 0:
        a, b = heapq.heappop(heap)
        a = -a

        if a != v[b]:  # 앞에서 값들을 많이 빼갔을 때, 힙을 업데이트 할 필요가 있음
            heapq.heappush(heap, (-v[b], b))

        else:

            if a > m - a + 1:  # 만족할 수 없음
                answer = []
                break

            elif a == m - a + 1:  # 최대 개수를 가진 사탕을 선택
                answer.append(b)
                v[b] -= 1
                heapq.heappush(heap, (-v[b], b))
                m -= 1

            else:
                num = m - 2 * a + 1  # num 개 까지는 그냥 가장 숫자가 큰 사탕을 빼도 됨 (Subtask 2 핵심)
                heapq.heappush(heap, (-a, b))

                for __ in range(num):
                    if index == answer[-1]:  # 똑같은 사탕이 연속해서 올 수 없음
                        answer.append(idx)
                        v[idx] -= 1
                        if v[idx] == 0:
                            idx += 1
                            while idx <  n:
                                if v[idx] != 0:
                                    break
                                else:
                                    idx += 1
                    else:
                        answer.append(index)
                        v[index] -= 1
                        if v[index] == 0:  # 사탕이 없으면 index 와 idx를 이동시켜야 함
                            index = idx
                            idx += 1
                        while idx <  n:
                            if v[idx] != 0:
                                break
                            else:
                                idx += 1
                    m -= 1

    if answer:
        ans = 0
        for i in range(1, len(answer)):
            ans = (ans + i * (answer[i] + 1)) % 987654323

        print(ans)
    else:
        print("IMPOSSIBLE")
