# print("대기번호", 1)

# for customer in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호", customer)

# for waiting_no in [1, 2, 3, 4, 5]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6):
#     print("기다리는 손님 : {0}".format(waiting_no))

#     =

# for waiting_no in range(1, 6):
#     print("기다리는 손님 : {}".format(waiting_no))

# for waiting_no in range(1, 6):
#     print("기다리는 손님 : {}".format(waiting_no))

# for waiting_no in range(1, 6, 2):
#     print("기다리는 손님 : {}".format(waiting_no))

# 6.22 조건을 만족할 동안 반복하기 : while 문
# while 조건 :
#     실행명령문
# # 조건이 참인 동안 계속 반복
# # 조건이 거짓이 되는 순간 반복문 종료

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))
#     index -= 1
#     print("{}번 남았습니다.".format(index))
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")


### 연습문

# customer = "최신우"
# index = 1

# while True:
#     print("{}님 강화를 시작합니다. 호출{}회".format(customer, index))
#     index += 1    
 
 # 컨트롤 + c : 무한루프 종료

# import time

# customer = "최신우"
# index = 1

# while index <= 10:
#     print("{}님 강화를 시작합니다. 호출{}회".format(customer, index))

#     if index == 5:  # 5회에서 멈추기
#         print("강화를 종료합니다.")
#         break       # while 문 강제 종료

# #     index += 1
# #     time.sleep(1)

# ## 응용
# import time
# import random

# customer = "최신우"
# index = 1
# numbers = list(range(1, 101))

# max_try = 1000  # 최대 시도 횟수

# while index <= max_try:
#     result = random.choice(numbers)
#     print("[시도 {}회] {}님 강화를 시도합니다... 뽑힌 숫자: {}".format(index, customer, result))

#     if result == 1:
#         print("축하합니다! 100분의 1 확률을 뚫고 강화에 성공했습니다!")
#         print("강화를 종료합니다.")
#         break

#     index += 1
#     time.sleep(0.1)

# if index > max_try:
#     print("아쉽지만 {}번 시도 동안 1이 나오지 않았습니다... 강화를 종료합니다.".format(max_try))

# customer = '최신우'
# person = None

# while person != customer:
#     print("{}님, 주문하신 무기 제작완료되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# absent = [2, 5]  # 결석

# # for student in range(1, 11):  # 1 ~ 10
# #     if student in absent:
# #         continue
# #     print("{0}번 학생, 출석체크 완료".format(student)) 

# # absent = [ 1, 5, 7]
# # no_book = [1, 3, 5, 7]

# # for student in range(1, 11):
# #     if student in absent:
# #         continue
# #     elif student in no_book:
# #         print("{}입니다. 책을 가져오지 않았습니다.".format(no_book))
# #         continue
# #     elif student in no_book:
# #         print("오늘 수업으 여기까지. {}번 한색은 교무실로 따라오세요.".format(student))
# #         break
# #     print("{0}번 학생, 책을 읽어보세요.".format(student))
# # 
# absent = [1, 5, 7]
# no_book = [1, 3, 5, 7]

# for student in range(1, 11):
#     if student in absent:          # 결석
#         continue                   # 밑에 코드 건너뛰고 다음 학생으로

#     elif student in no_book:       # 책 안 가져온 학생
#         print("{}번 학생은 책을 가져오지 않았습니다.".format(student))
#         print("오늘만 봐준다. {}번 학생은 방과후 교무실로 따라오세요.".format(student))
#         break                      # 반복문 완전히 종료

#     else:                          # 정상 출석 + 책 가져옴
#         print("{0}번 학생, 책을 읽어보세요.".format(student))

#         absent = [1, 5, 7]        # 결석한 학생
# no_book = [1, 3, 5, 7]    # 책 안 가져온 학생

# # 정원 10명: 1번 ~ 10번까지 전원 체크 (수업이 중간에 끝나지 않게 break 사용 X)
# for student in range(1, 11):
#     # 1. 결석한 학생
#     if student in absent:
#         print("{}번 학생은 결석했습니다.".format(student))
#         continue          # 아래는 건너뛰고 다음 번호로

#     # 2. 책을 안 가져온 학생
#     if student in no_book:
#         print("{}번 학생은 책을 가져오지 않았습니다.".format(student))
#         print("오늘 수업은 여기까지. {}번 학생은 교무실로 따라오세요.".format(student))
#         # 정원 10명 전부 확인해야 한다고 했으니까 break 하지 않고 그냥 계속 진행
#         continue

#     # 3. 정상 출석 + 책도 가져온 학생
#     print("{0}번 학생, 책을 읽어보세요.".format(student))

# 6.24 for 문 한줄로 작성하기
# 동작 for 변수 in 반복대상

# student = [1,2,3,4,5]
# print(student)

# student = [ i  + 100 for i in student]
# print(student)

# 같은문장
# students = [1, 2, 3, 4, 5]
# sutdents = [sutdents[0] + 100 , students[1] + 100, studenst[2] + 100, students[3] + 100, students[4] + 100]
# print(student)

#6.24.1 연습문제
st = ["Iron man", "Thor", "spider man"]
print(st)

# st = [len(i) for i in st]
# print(st)

st = [i.upper() for i in st]
print(st)

