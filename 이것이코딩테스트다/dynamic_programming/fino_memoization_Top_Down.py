# 한번 실행된 결과를 저장 해두는 리스트 초기화
memo = [0] * 100

# 피보나치 함수 재귀함수로 구현
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산된적 있다면 그대로 반환
    if memo[x] != 0:
        return memo[x]
    
    # 계산을 실행하고 저장한다
    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]

print(fibo(99))
