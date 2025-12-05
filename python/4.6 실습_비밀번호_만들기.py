a = "https://naver.com"

def clean_a(a):
    if a.startswith("https://"):
        a = a[8:]
    elif a.startswith("http://"):
        a = a[7:]
    
    for ext in [".com", ".net", ".co.kr", ".org"]:
        if a.endswith(ext):
            a = a[:-len(ext)]
            break

    return a

# 함수 결과를 변수 b에 저장
b = clean_a(a)
print(b)   # naver

# b의 앞 3글자만 c에 저장
c = b[:3]
print(c)   # nav

d = b.count('e')
print(d)

e = "!"
print(e)

password = (c + str(d) + e)
print(password)

NAVER = a+'의 비밀번호는 ' +password+ '입니다.'
print(NAVER)

#2번

a = 'https://daum.com'

len = len(a)
print(len)

d위치 = (a.index('d'))
print(d위치)

m위치 = (a.index('m'))
print(m위치)

bb = a[8:12]
print(b)

b = str(bb)
print(b)

pp = b[0:3]
print(pp)
p = str(pp)
print(p)

ss = (a.count("e"))
print(ss)
s = str(ss)
print(s)

w = "!"

password = (p+s+w)
print(password)

print(a+'의 비밀번호는'+password+' 입니다.')


#3 gpt 풀이

def make_password(url):
    # 1) http://, https:// 제거
    url = url.replace("https://", "").replace("http://", "")
    
    # 2) 끝 확장자 제거
    for ext in [".com", ".net", ".co.kr", ".org"]:
        if url.endswith(ext):
            url = url[: -len(ext)]  # 여기서 len() 사용 가능
            break

    # 3) 앞 3글자
    first3 = url[:3]

    # 4) 'e' 갯수
    e_count = url.count("e")

    # 5) 비밀번호 생성
    password = first3 + str(e_count) + "!"
    
    print(f"{url} → 비밀번호: {password}")
    return password


a = "http://gogole.com"
pw = make_password(a)
print(a + "의 비밀번호는 " + pw + " 입니다.")


#4 gpt따라 연습 및 학습이해하기

