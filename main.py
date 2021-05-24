# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''value = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(value1)'''



'''for i in range(10) :

    for j in range(10-i):

        print("*", end="")
    print("")'''
'''print(list(range(1,10,2)))

for i in range(11):
    print(i[1:6], end="")'''


'''i= "A B C D E"
for i in range(5):
    print("A B C D E", end="")'''
'''student=[["kim",90], ["park", 100]]
for i in range(0, 2):
    print(student[i])
sum=0
for i in range(0,2):
    print(student[i][0])
    print(student[i][1])
    sum=sum+ student[i][1]

print(sum)'''
'''name=["park", "kim","lee","choi"]
name. remove("kim")
print(nal'''
'''letters1=["Aa", "Bb", "Cc"]
letters1= dict(letters1)
print(letters1)
names=("kim", "lee", "park", "choi")
scores=(90, 80, 70, 60)
student=dict(zip(names, scores))
print(student)
print(student["kim"])
menu=("coffee","juice","water")
price=(500,1000,2000)
my_menu=dict(zip(menu,price))

print(my_menu["juice"])
my_menu["juice"]=3000
print(my_menu)'''
'''list1=[]
list2=[]
value=0
for i in range(5):

    for k in range(5-i):
        list1.append(value)
        value=value+3
    list2.append(list1)
    list1=[]
for i in range(5):


    for k in range(5-i):
        print("%3d" %list2[i][k], end="")
    print("")'''

'''for i in range(10-i):
    for k in range(5-i):
        print("*", end="")'''
a = ["abc", "def", "ghi", "jkl", "mno"]
'''for x in range(6):
    print("")
    for i in range(6-x):
        print(" ", end="")
    for k in range(1+2*x):
        print("*", end="")
for x in range(9):
    print("")
    for i in range(x):
        print(" ", end="")
    for k in range(11 - 2*x):
        print("*", end="")'''
'''for i in range(5):

    for x in range(5-i):
        print(" ", end="")
    for z in range(i):
        print("*", end="")
    print("")'''
'''k=10
for k in range(10):
    if k>4:

    for x in range(1,k+1):
        print(" ", end="")
    for z in range(k-1):
        print("*", end="")
    print("")'''
'''else:
    for x in range(i+1):
        print(" ", end="")
    for z in range(7-2*i):
        print("*", end="")
    print("")'''


'''for i in range(5):
fesdfdsfsdfdsfdsffdsfdsffdsfsf
    for x in range(i+1):
        print(" ", end=""fdsfsdffdsfdsfdsfsfdsfdsfdsfdsfsdfdsdsfds)
    for z in range(7-2*i):
        print("*", end="")
    print("")'''

'''k = 5
for i in range(10):
    if i <= int(k/2)+1:
        for j in range(4 - i - 1):
            print(" ", end="")
        for j in range((i * 2) + 1):
            print("*", end="")

    else:
        for j in range(i + 5):
            print(" ", end="")
        for j in range(10 - (i * 2)):
            print("*", end="")
    print("")'''

''''#BMI연산프로그램
weight=float(input("몸무게를 입력해 주세요:"))
height=float(input("키를 입력해 주세요(m)"))
sum=weight/height
bmi=sum/height
print("나의BMI는",bmi,"입니다")
if bmi<18.5:
    print("저체중 입니다")
elif 18.5<bmi<23:
    print("정상체중 입니다.")
elif 23<bmi<25:
    print("과체중 입니다.")
else:
    print("비만입니다.)'''
# **햄버거 주문 프로그램
# 1. 햄버거 2. 음료 3. 사이드메뉴  4.계산
# 할당
'''price = 0


while (1):

    print("---------------------------------------------------")
    print("                햄버거 주문 화면입니다             ")
    print("---------------------------------------------------")
    d = {"싸이버거": 4000, "새우버거": 5000, "치즈버거": 6000}
    print(d)
    print("---------------------------------------------------")

    menu2 = input("원하는 햄버거 메뉴를 입력하세요")
    print(d[menu2])
    print("%s 를 주문하셨습니다." % menu2)
    print("가격은 %d 입니다" % (d[menu2]))
    price=price+d[menu2]



    print("**************")
    print("선택해주세요")
    print("**************")
    menu3 = input("세트 or 단품 ")
    c={"세트":2000, "단품": 0}
    print("---------------------------------------------------")
    print("%s를 주문하셨습니다." % menu3)
    print(" %d원이 추가되었습니다. " % (c[menu3]))
    price = price + c[menu3]
    print("---------------------------------------------------")


    menu4 = int(input("개수를 입력해주세요"))

    if menu4 == 1:
        print("---------------------------------------------------")
        print("                  감사합니다                       ")
        print("---------------------------------------------------")
    if menu4 >= 2:
        print("---------------------------------------------------")
        print("                  감사합니다                       ")
        print("---------------------------------------------------")
        price = price*menu4
    menu = input("주문을 마치시겠습니까? y/n")
    if (menu == "y"):
        print("주문을 종료하게습니다.")
        print("-" * 60)

        print("             주문가격은", price, "입니다.")
        print("                맛있게 드세요                  ")
        print("-" * 60)

        exit()

    else:
        continue'''

'''def add(a,b):
    return a+b
value1=10
value2=20
print(add(value1,value2))
def muti(a,b,c,):
    return a*b*c
print(muti(10,20,30))
def para2_fuc(v1,v2):

    result= v1+v2
    return result
hap = para2_fuc(10,20)
print(hap)
def para_fun(*para):'''


'''<<BMI 계산을 위한 예시함수를 주었는데 질문이 많아 제가 간단한 설명 드립니다.>

//함수의 정의
def calcBMI(height, weight) :
     return weight/(height*height)   //이때 height는 미터로변환해야 함 (키가 170인 경우 1.7로 변환) 키 / 100으로 하면 됩니다. 단, 정수/정수=>정수 주의 

def myBMI(result) :// 이 함수는 calcBMI 함수의 결과값을 전달받아 myBMI 결과를 출력하는데 사용합니다.
    if result>=30:
           print("당신은 고도비만입니다")
     elif result>=25.:
        이와 같이 작성한 후...

//함수의 호출
result = calcBMI(height, weight) //호출하여 result에 리턴 받음
myBMI(result) 호출                       //reuslt값을 myBMI의 매개변수로 전하여받아 비만여부르 출력합니다.


//myBMI 다른 작성예
def myBMI(result) : 
    if result>=30:
           re = "고도비만"
     elif result>=25.:
           re = "비만"
     이런식으로 작성하여 myresult = myBMI(result)와 같은식으로 함수를 호출하여 myresult를 출력해도 됩니

def calbmi(height, weight):
    return weight / (height * height)



def mybmi(result):
    if result>=30:
        print("고도비만입니다.")
    elif result>=25 and result<30 :
        print("과체중입니다")
    elif result>=19 and result <25:
        print("정상입니다.")
    else:
        print("저체중 입니다.")
b=float(input("키를 입력하세요."))
c=float(input("몸무게를 입력하세요."))
result=calbmi(b,c)
print("bmi는 %d 입니다" %result)

mybmi(result)
#기본 잔액은 10000원으로 설정
mm=10000
def cal(a,mm=10000):

    mm=a+mm
    print("입금금액은 %d원입니다"%a)
    print("고객님의 잔액은 %d 원입니다." %mm)
    return" "

def cal2(b,mm=10000):
    if b>mm:
        print("출금할 수 없습니다.")
        return" "

    else:
        mm = mm-b
        print("출금금액은 %d원입니다" % b)
        print("고객님의 잔액은 %d 원입니다." % mm)
        return" "


while (2):
    print("경기ATM기 입니다")
    print("다음메뉴를 선택하세요")
    print("*" * 40)
    print("1.입금 2.출금 3.종료")
    print("*" * 40)
    d= float(input("번호를 입력하세요"))
    if d==1:
        e=float(input("출금액을 입력하세요"))
        cal(e)
    elif d==2:
        g=float(input("출금액을 입력하세요"))
        cal2(g)
    else:
        break
list1=[]
list2=[]
b=int(input("과목수를 입력하세요"))
for x in range(b):
    a=float(input("번호를 입력하세요"))
    list1.append(a)
print(list1)
b=int(input("과목수를 입력하세요"))
for x in range(b):
    c=float(input("번호를 입력하세요"))
    list2.append(c)
print(list1*list2)
https://api.odcloreer.kr/api/v1/centers?page=1&perpage=

import requests
import json

url = 'https://api.odcloud.kr/api/15077586/v1/centers'
param={'page':1, 'perpage' :10, 'serviceKey': 'LROuCFeMjOxxJPV+ivgk2Zj+2PMI+L8teZ/0kreP8EbbdeNeAHkRTtwbwS6OikOHaK7YV86lVLihqapyoIhhiw=='}

response = requests.get(url, params=param)

print(response.text)

a=json.loads(response.text)
print(a['data




def triangle_fun():
    global list1
    if max(list1)<sum(list1)-max(list1):
        print("삼각형이 성립합니다.")
    else:
        print("삼각형이 성립하지 않습니다.")

while(1):
    list1 = []
    for i in range(3):
        x = int(input("삼각형의 각도를 입력해 주세요"))
        list1.append(x)

    if sum(list1) == 180:

        triangle_fun()

    else:
        print("삼각형 내각의 합이 180이 아닙니다."
              "다시 입력해 주세요)'''
























































