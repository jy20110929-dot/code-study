def pw(a):
    a = a.replace("https://", "").replace("http://", "").replace("www.", "")
    for end in [".com", ".net", ".co.kr", ".org"]:
        if a.endswith(end):
            a = a[:-len(end)]
            break

    f3 = a[:3]
    e = a.count("e")
    pr = f3 + str(e) + "!"
    print(f3)
    return pr

naver = "https://www.naver.com"
daum = 'https://www.daum.net'
youtube = 'http://www.youtube.com'

naver_pw = pw(naver)
daum_pw = pw(daum)
youtube_pw = pw(youtube)


print(f"네이버의 비밀번호는 {naver_pw} 입니다.")
print(f"다음의 비밀번호는 {daum_pw} 입니다.")
print(f"유튜브의 비밀번호는 {youtube_pw} 입니다.")




