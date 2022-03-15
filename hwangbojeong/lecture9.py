##리스트
my_list = [1, 2, 3]
student = ['메이충리엘', '황보정', '아무개']
print(student)
import random
print(random.choice(student))
student.append('박창현') #리스트에 추가
print(student)

student[1] = '이규석' # change
print(student)
my_tuple = ( '이규석', '황보정', '김민섭')
#tuple 값변경 불가능


my_dict = {'황보정' : '남 ', '박창현' : '여 ', '이규석' : '코인 '}
print(my_dict['황보정'])
print(my_dict['이규석'])
my_dict['박창현'] = '남'
print(my_dict['박창현']) # 수정
#dict => 키와 값값