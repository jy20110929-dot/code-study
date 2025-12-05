
a = 'Amazing is Python'
print(a.lower())

print(a.upper())

print(a[0].isupper())

print(a[1:5].islower())

print(a.replace("Python", "Java"))

text = "python"
b = text[4]   # 인덱스 0부터 시작: p(0) y(1) t(2) h(3) o(4) n(5)
print(b)      # o 가 나옴 → n은 5번 인덱스


s = "abcdefghijklnmopqrstuvwxyz"

print(s.index("a"))   # 0
print(s.index("k"))   # 11 (공백, 글자 다 포함해서 0부터 셈)
print(s.index("z"))   # 마지막 위치 번호
print(s.find("B"))
# print(s.index("B")) #오류발생함 그래서 find는실패하면 -1로 지정할수가 있음 하지만 index는 찾지못하며 오류가남
print(s.find("z",1,10)) # 1번째에서 10까지 찾아보니 안보여서 
print(s.find("k",1,11)) # 10번까지라 10번인 k탐색은 11번까지를 부여해야함
print(s.find("b",1,11)) # 1부터라 b를찾을수있음

sw = 'aaaaaaaaaabbbbbbbbbbbbbbbbbbbccccccccccccccccccccc'
print(sw.count("a")) #a가 몇개인지
print(sw.count("b"))
print(sw.count("c"))
print(len(sw)) # 길이측정

