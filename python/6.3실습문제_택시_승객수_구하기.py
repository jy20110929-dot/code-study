from random import randint

total_customers = 50      # 전체 손님 수
matched_count = 0         # 조건(5~15분) 맞는 손님 수

for customer in range(1, total_customers + 1):
    time = randint(5, 50)   # 5~50분 사이 난수로 소요 시간 생성

    if 5 <= time <= 15:     # 5분 이상 15분 이하인 손님만 매칭
        print("[O] {0}번째 손님 (소요 시간: {1}분)".format(customer, time))
        matched_count += 1
    else:
        print("[ ] {0}번째 손님 (소요 시간: {1}분)".format(customer, time))

print("총 탑승객 : {} 명".format(matched_count))
