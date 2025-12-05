## List, Set, Tuple 변환이 자유롭다

## 자료구조확인은 type으로 하다.

## 1 - 1

# menu = ['김밥', '라면', '튀김']
# print(menu)
# print(type(menu))

# menu = set(menu)
# print(menu)
# print(type(menu))

# menu = tuple(menu)
# print(menu)
# print(type(menu))

## 1 - 2 
## 문제2
my_list = [1, 2, 3, 4, 4, 4 ,5]
my_set = set(my_list)
# my_list = list(my_set)
print(my_list) # my_set을 리스트로 명령만 줫기때문에 세트효과 없음 당연한거다