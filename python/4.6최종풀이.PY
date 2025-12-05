def pw(link):
    link = link.replace("https://", "").replace("http://", "").replace("www.", "")
    
    for end in [".com", ".net", ".co.kr", "org"]:
        if link.endswith(end):
            link = link[:-len(end)]
            break

    first3 - link[:3]

    e_count = link.count("e")

    psw = first3 + str(e_count) + "!"
    return psw

naver = "https://naver.com"
daum = 'https://daum.net'
youtube = 'http://youtube.com'

naver_pw = pw(naver)
daum_pw = pw(daum)
youtube_pw = pw(youtube)

print(f"네이버의 비밀번호는 {naver_pw} 입니다.")