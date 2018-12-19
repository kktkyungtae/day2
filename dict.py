"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")

iu = {"수학" : 80, "국어" : 90, "음악":100}
average = sum(iu.values()) / len(iu)
print(average)

#1. iu_score라고 하는 dic변수에서 valu값만 뽑아내 보자
#2. 뽑아낸 값의총 합을 구한다.
#3. 총합의 개수로 나눈다


total_score = 0
count=0
for score in iu_score:
    total_score = total_score + iu_score[score]
    count = count + 1
#    print(total_score/count)
scores = list(iu_score.values())
print(list(scores))



# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")


iu = {"수학" : 80, "국어" : 90, "음악":100}
ui = {"수학" : 80, "국어" : 90, "음악":100}

average = sum(iu.values()) / len(iu)
average2 = sum(ui.values()) / len(ui)

print(average)
print(average2)



# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
#1. 각 도시를 순회하는 반복문을 작성한다.
for city in cities:
    print(cities[city])
    temp = cities[city]

#2. 1번의 코드를 활용하여 순회할 때마다 평균값을 출력한다.
    print("{}의 평균기온 : {}입니다.".format(city,round(sum(temp)/len(temp),1)))
    print("{}의 평균기온 : {:0.1f}입니다.".format(city,round(sum(temp)/len(temp),1)))




# 3-1. 도시 중 최근 3일에서 가장 추웠던 곳, 가장 더웠던 곳은?
# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")


#2. 최저기온, 최저기온을 저장할 수 있는 공간을 선언한다.
minimum = {"도시명" : 1000}
maximum = {"도시명" : -1000}

#1. 각 도시를 순회하는 반복분을 만든다
for city in cities:

#3. 각 도시의 기온 정보를 순회하는 반복문을 만든다.
    for temp in cities[city]:
 
#4. 순회하다가 최저기온의 경우에는 현재 저장된 값 보다 작은값이,
# 최고 기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우
# 현재 저장되어 있는 값을 바꾼다.
        #최고 기온에 해당하는 조건문
        if(maximum[1] < temp):
            maximum[0] = city
            maximum[1] = temp
        
        #최저 기온에 해당하는 조건문
        if(minimum[1] > temp):
            minimum[0] = city
            minimum[1] = temp
print("최고 기온의 {}은 {}도이며, 최저 기온은 {}의 {}도 입니다.".format(maximum[0], maximum[1], minimum[0],minimum[1]))


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")

#1. cities 변수에서 서울부분만 추출해서 seoul 변수에 저장한다.
#1-1. flag 라고 하는 변수에 false를 저장한다.
#2. seoul 변수(list)를 순회하며 요소가 2와 같았던 적이 있는지 확인한다.
#3. 2도와 같았던 적이 있다면 flg 변수를 true로 바꿔준다. 
#4. flag 변수에 따라 출력문을 작성한다.