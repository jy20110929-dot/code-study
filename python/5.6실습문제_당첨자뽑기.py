## 1-1
## 문제 : 파이썬 코딩대회 열립니다.
## 참석률을 높이기 위해 댓글 이벤트를 진행했습니다.
## 댓글에 닉네임을 적어준 사람들 중 추첨을 통해 3명에게 커피 쿠폰을 드립니다.
## 추첨 프로그램을 작성하시오.

### 조건
### 편의상 댓글은 20명이 작성했고. 아이디어는 1~20이라고 가정한다
### 무작위로 추첨하되 중복은 허용하지 않는다.
### random 모듈의 sample() 함수를 활용해보자
### 실행결과를 만들어보자

#### -- 담청장 발표 --
#### 치킨 당첨자 : 6
#### 커피 당첨자 : [9, 3, 10]
#### - 축하합니다! --


# ## 내풀이
# import random
# drawer_list = list(range(1,21))
# random.shuffle(drawer_list)
# ck_winner = random.sample(drawer_list,1)[0]
# cf_winner = random.sample(drawer_list,3)
# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {ck_winner}")    
# print(f"커피 당첨자 : {cf_winner}")
# print("-- 축하합니다! --")

## gpt 풀이
# import random

# drawer_list = list(range(1, 21))  # 1~20번 댓글 작성자

# # 치킨 당첨자 1명 뽑기
# chicken_winner = random.sample(drawer_list, 1)[0]  # sample은 리스트 반환하므로 [0]으로 꺼냄

# # 커피 당첨자 3명 뽑기
# coffee_winners = random.sample(drawer_list, 3)  # 중복 없이 3명 뽑음

# # 결과 출력
# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {chicken_winner}")
# print(f"커피 당첨자 : {coffee_winners}")
# print("-- 축하합니다! --")


## suple 미사용에 대한 지적

# from random import *

# lst = [1, 2 , 3, 4, 5 ]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

## 마무리 문제

list = ['자료구조', '알고리즘', '자료구조', '운영체제']
print(type(list))
print(list)
set_list = set(list)
print(set_list)

list = {'자료구조', '알고리즘', '자료구조', '운영체제'}
print(type(list))
print(list)