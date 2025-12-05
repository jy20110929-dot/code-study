sentence1 = '나는 소년입니다.'
print(sentence1)

sentence2 = "파이썬은 쉬워요."
print(sentence2)

sentence1 = '나는 소년입니다.'
print(sentence1, type(sentence1))
sentence2 = '파이썬은 쉬워요.'
print(sentence2, type(sentence2))

sentence3 = "나는 소년이고, 파이썬은 쉬워요"
print(sentence3, type(sentence3))

sentence4 = """나는 3.0이고 파이썬은 3.18이에요."""
print(sentence4, type(sentence4))

sentence4 = "나는 3.0이고 파이썬은 3.18이에요."
print(sentence4, type(sentence4))

print("파인"+"애플")
print("파인","애플")
print("파인 + 애플")
print('"파인"+"애플"')
print('"파인"+"애플"')

jumin = "920528-1103219"
print("성별 식별번호 : " + jumin[7])
jumin = "920528-1103219"
print("출생년도 식별번호 : " + jumin[0:2])

#제대로하기

jumin = "920528-1103219"
print("연 : "+jumin[0:2])
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])
print("성별 : "+jumin[7])
print("지역번호 : " +jumin[8:12])
print("등록순서 : " +jumin[12])
print("검증번호 : " +jumin[13])

print("주민번호 : "+jumin[:14])
print("주민번호 : "+jumin[0:])
print("주민번호 : "+jumin[1:])
print("생년월일 : "+jumin[:6])
print("주민뒷자리 : "+jumin[7:])

fruit = 'apple'
print(fruit[:-1])

