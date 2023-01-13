## 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수
## 1924에서 수 두개를 제거->[19,12,14,92,94,24]
## 문자열 형식으로 숫자 number와 제거할 수의 개수 k
## number에서 k개의 수를 제거했을 때 만들 수 있는 가장 큰 수 문자열 형태

## greedy한 경우를 찾자 -> 전체의 경우를 선택

## 문자열을 list로 받아서 join을 이용하여 추출
## ''.join(list)

## 풀이
def solution(number, k):
    answer = ''
    answer_list=[]
    number_list=[]

    ## number을 list로 받기
    number_list = list(number)

    ## k만큼 제거한 수를 answer_list에 append
    

    return answer
