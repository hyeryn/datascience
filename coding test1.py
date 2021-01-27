# 1

a = []
b = []
for i in range(0,10) :
    if i % 2 == 0 :
        a.append(i)
    else :
        b.append(i)
print(a,b)

#2

a = print(type(10)) # int - 정수형
b = print(type((1.44,'bitamin'))) # 튜플 - 리스트와 사용법은 유사하지만, 읽기전용 자료를 저장하는데 사용 + 수정과 삭제가 안된다
c = print(type("비타민")) # 스트링 - 문자열
d = print(type([1,2,3,4,5])) # 리스트 - 동일한 type의 변수들의 집합 (배열의 개념과 유사) + 수정과 삭제가 자유롭다
e = print(type({"특별시":"천안","충남":"서울","인천":"광역시"})) # 딕셔너리 - 키와 값의 쌍으로 구성되어있는 자료구조

#3

score = [90,25,67,45,80]
for i in range (0,5):
    if score[i] >= 80:
        print("우수")
    elif score[i] < 80 and score[i] >= 60:
        print("보통")
    else :
        print("미흡")
        
#4
 
import seaborn as sns
titanic=sns.load_dataset('titanic')
titanic.head(3)

df = titanic
df = df.loc[:,['pclass','fare']]

z_score = lambda x: (x-min(x))/(max(x)-min(x))
df.fare = (z_score(df.fare))
df.head(3)

#5

import pandas as pd
from google.colab import drive
drive.mount('/content.drive')

filename = '/content/insurance2.csv'
df = pd.read_csv(filename)
df.head(8)

df.fillna(method="ffill")
