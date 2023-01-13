## 학생들의 번호는 체격 순으로 부여
## 옷을 빌려 줄 땐 앞 뒤 사람만 가능

## 전체 학생의 수 n, 체육복을 도난당한 학생들의 배열 lost
## 여벌의 체육복을 가저온 학생들의 번호가 담긴 배열 reserve

# 체육수업을 들을 수 있는 학생의 최댓값을 return

# 제한 사항 #
# 전체 학생의 수 -> 2명 이상 30명 이하
# 도난당한 학생의 수 -> 1명 이상 n명 이하, 중복 번호는 없다
# 여분의 옷을 가져온 학생 중에서도 도난당한 학생이 있을 수 있다

###### 포인트는 여분을 기준으로 생각하는 것
# 내가 헤맨 이유는 lost를 기준으로 생각했기 때문이다

## solution -> set으로 푸는 방법
## 집합의 경우 합집합(&), 교집합(|), 차집합(-)을 사용할 수 있어서 편하다

## 도난도 당하고 여분도 들고온 경우 제거
def solution(n, lost, reserve):
    answer = 0
    lost_only = set(lost) - set(reserve)
    reserve_only = set(reserve) - set(lost)

## reserver를 기준으로 생각
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)


## 결과 출력
    answer = n - len(lost_only)
    return answer

#########################
########### 리스트로 푸는 방법
def solution(n, lost, reserve):
    ## 중복의 경우 제거
    lost_only = [l for l in lost if l not in reserve]
    reserve_only = [r for r in reserve if r not in lost]

    ## set으로 해결했던 것과 같이 리스트로 해결
    for i in reserve_only:
        front = i - 1
        back = i + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    
    ## 결과 출력
    answer = n - len(lost_only)
    return answer

#########################
############ 배열로 푸는 방법
def solution(n, lost, reserve):
    answer = 0
    ## student 배열 생성
    student = [0] * (n+2)

    ## lost(-1)와 reserve(+1)정보 저장
    for r in reserve:
        student[r] += 1
    for l in lost:
        student[l] -+ 1

    ## 여분이 있는 사람을 기준으로 앞뒤를 살피면서 제공한다.
    for i in range(1, n+1):
        # 만약 양수이면 == 여분이 있다면
        if student[i] > 0:
            front = i - 1
            back = i + 1
            if front < 0:
                student[front] += 1
                student[i] -= 1
            elif back < 0:
                student[back] += 1
                student[i] -= 1

    ## student배열에서 0보다 큰 학생 수 계산하면 정답 -> 0은 하나를 가지고 있는 것이고, 1이면 2개를 가지고 있는 것이므로
    
    for i in range(1,n+1):
        if student[i] >= 0:
            answer += 1
    
    return answer