# # 세트명 = {value1, value2 ....}

# my_set = (1, 2, 3, 3, 3)
# print(my_set) #세트가아니라서 1 2 3 3 3 다출력됨

# my_set = [1, 2, 3, 3, 3]
# print(my_set) #동일함

# my_set = {1,2,3,3,3}
# print(my_set) # 1, 2, 3 만나옴 3이묶여졌죵

java = {'푸', '피글렛', '티거'}
python = set(['푸','이요르'])

print(java & python)
print(java.intersection(python))

## 합집합 union 이나 | 사용하면됨 
## 세트는 데이터 순서를 보장하지않음, 세트에 저장한값을 출력하면 매번변험
# print(java | python)
# print(java.union(python))

# ## 차집합 - 이나 difference 
# print(java - python)
# print(java.difference(python))

## 추가 .add (mathod)
# python.add("피글렛")
# print(python)

# python.remove("피글렛")
# print(java)


