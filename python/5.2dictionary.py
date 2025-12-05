# empty_dick = {} #빈딕셔너리

# cabinet = {3:"푸", 100:"피글렛"}
# print(cabinet.get(3))
# print("hi")
# print(cabinet[3])
# print("hi")

# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(5, "사용가능"))

# print(3 in cabinet)
# print(5 in cabinet)

#chatper 2 @@@@@@@@@@@

# cabinet = {"A-3":"푸","B-100":"피글렛"}

# print(cabinet["A-3"])
# print(cabinet["B-100"])

#chapter 3 @@@@@@@@@@@@
# print("곰" in "곰돌이")

# del cabinet["A-3"]
# print(cabinet)

# 5.23 값 확인하기
cabinet = {"A-3":"푸","B-100":"피글렛"}
cabinet["A-3"] = '티거'
cabinet["C-20"] = '이요르'
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items)

