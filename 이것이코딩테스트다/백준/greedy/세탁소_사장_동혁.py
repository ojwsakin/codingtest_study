## 리암이의 거스름돈 실수
## Quarter - $0.25
## Dime - $0.10
## Nickel - $0.05
## Penny - $0.01

## 거스름돈은 항상 $5.00이하

####### 플이 #########
# 함수
def cal(money):
    Quarter = money // 25
    Dime = (money % 25) // 10
    Nickel = (money - (Quarter * 25) - (Dime * 10)) // 5
    Penny = (money - (Quarter * 25) - (Dime * 10) - (Nickel * 5))
    
    print(Quarter, Dime, Nickel, Penny)

# 입력
t = int(input())

## 테스트케이스 리스트 append
money = []
for i in range(t):
    money.append(int(input()))

## 생성한 함수에 의해 출력
for i in money:
    cal(i)