print('a','b')
print('a'+'b')
print('나는 %d살 입니다.'%20) #정수표현이가능함``
print('나는 %s살 입니다.'%23)
print('나는 %c살 입니다.'%'네')
print('나는 %f살 입니다.'%23)
print('나는 %s살 입니다.'%'스무세')

print('나는 {}살 입니다.'.format(20))
print('나는 {}색과, {}을 좋아합니다.'.format('파랑','빨강'))
print('나는 {0}색과, {1}을 좋아합니다.'.format('파랑','빨강'))                      
print('나는 {1}색과, {0}을 좋아합니다.'.format('파랑','빨강'))                      
print('나는 {1}색과, {1}을 좋아합니다.'.format('파랑','빨강'))        

print('나는 {age}실이며, {color}색을 종아합니다.'.format(age=20, color='빨강'))

age=20
c = '빨'
print(f"나는 {age}살이며, {c}색")
