# 1-1 if 기초
# weather = '비'
# if weather == '비':
#     print("우산을 챙기세요")

#1-2 if 문 들여쓰기

# if와 같은열이면 조건을 안받고 항시 실행
#2 if문 내에 실행하면 if가 참일때 하단내용 실행
#3 if문 1문이 {} 중괄호를 받앗다면 두번째내용은 같은열이어도 항상 실행이된다.

# 6.1.2 조건이 여러 개일때 : elif

# weather = '맑음'
# if weather == '비':
#     print("우산을 챙기세요") # 값이 없으므로 실행안됨

# weather = []'미세먼지', '눈']
# if weather == '비':
#     print("우산을 챙기세요")            
# elif weather == '미세먼지':
#     print("마스크를 챙기세요")  
#     print("실내에 머무르세요")

# elif weather == '눈':
#     print("눈이오니 따뜻하게 입으세요")

# 6. 1. 3 모든 조건이 맞지 안을때 
# weather = '맑음'
# if weather == '비':
#     print("우산을 챙기세요")            
# elif weather == '미세먼지':
#     print("마스크를 챙기세요")  
# elif weather == '눈':
#     print("눈이오니 따뜻하게 입으세요")
# else:
#     print("준비물이 필요없어요")

# 6. 1. 4 input으로 입력받기
# weather = input("오늘 날씨는 어때요? ")  # 사용자가 입력
# print(weather) # 터미널에서 답장을하면 그값이 실행됨

# if weather == '비':
#     print("우산을 챙기세요")
# elif weather == '미세먼지':
#     print("마스크를 챙기세요")
# elif weather == '눈':
#     print("눈이오니 따뜻하게 입으세요")
# else:
#     print("준비물이 필요없어요") 

# or 연산자
# weather = input("오늘 날씨는 어때요? ")  # 사용자가 입력
# print(weather) # 터미널에서 답장을하면 그값이 실행됨

# if weather == '비' or weather == '눈': # 조건변경
#     print("우산을 챙기세요")
# elif weather == '미세먼지':
#     print("마스크를 챙기세요")
# elif weather == '눈':
#     print("눈이오니 따뜻하게 입으세요")
# else:
#     print("준비물이 필요없어요")

temp = int(input('오늘 기온은 어때요?'))

if 30 <=temp:
    print('너무 더워요. 외출을 자제해주세요')
elif 10 <=