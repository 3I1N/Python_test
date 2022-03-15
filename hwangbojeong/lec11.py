## comment -> 주석 , 컴터는 못알아들음(무시)
print('hello world')  # ㅎㅇ
print(2+3) #5
#lec 12 string
# 문자열 값 , 순서 변경 못함
my_str = "정씨가족"

print(my_str)

type(my_str)
print(type(my_str)) #문자열 자료형

my_str = '황보정 박창현'
print(my_str)
print(type(my_str))

my_str = """황보정 
박창현 
이규석
"""
print(my_str) #세개는 여러 줄 사용가능

#Formatting -> 문자열 잘 표현하기 위함 (%..)

my_str = 'My name is %s' %'young jeong'
print(my_str) #young jeong이 %s로 대입

print('%d %d' % (1,2)) # %d는 정수형 숫자 대입 두개이상 괄호
print('%f'% 3.14) # %f는 실수

# format() ?
print('my name is %s' % '황보정')

print('my name is {}'. format('콩')) #format 중괄호 사용

print('{} * {} = {}'.format(3, 2, 3*2))
print('{1} x {0} = {2}'.format(2, 3, 3*2)) # 앞에는 순서 0,1,2 순

# indexing 위치 주소 ( 0부터 시작 항상 )

my_name = "김왼손의 왼손코딩"
print(my_name[1]) #공백도 생각해야함
print(my_name[4])
# -주소도 가능 .. 뒤로 시작
print(my_name[-1])

# Slicing 여러개 뽑아오기
print(my_name[2:4]) # 4전까지 떼어 옴
print(my_name[5:7])
print(my_name[:3]) #앞부터 3전까지
print(my_name[2:]) # 2부터 끝
print(my_name[:]) # 다 , 문자열은 그대로 있고 값만 복사해서 오는것

# string.split() 메서드 , 문자열 공백 단위로 잘라줌
print(my_name.split())
fruit_str = '거봉 수박 딸기 포도 사과 배'
print(fruit_str.split())
fruits = fruit_str.split()
print(fruits)
brand_str = '삼성 : 애플 : 엘쥐 '
brands = brand_str
print(brands.split(':')) # (:) 면 : 마다 구분 지어라 는 뜻
# [] 대괄호는 list

# Docsting
"""이것도 주석이지롱""" #Docsting

#print('',end='')
print('집단지성')
print('집단지성', end='') #끝에 추가









