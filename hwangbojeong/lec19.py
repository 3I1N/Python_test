# Escape code
# \n 줄바꿈 \t 는 뛰는 것
print('미운정이샛기의 집들')
print('미운정이샛기의\n집들')
print('미운정이샛기의\t집\n들')
print('미운', end='\t');
print('코딩')  # ;하면 끝낼수 있음

# list 여러 값 모아서 저장
my_list = []
print(my_list)  # 빈 리스트
print(type(my_list))
my_list = [1, 2, 3]
print(my_list)

std = ['하이', '바이', '굿바이']
print(std)
std.append('애프터눈')  # append는 list에만 사용가능
print(std)

animals = []
animals.append('코알라')  # append는 1씩만 추가 가능, 빈 리스트가 있어야 함
print(animals)

# list indexing
print(std)
animals.append('하이네나')
animals.append('바보')
animals.append('호랑이')
animals.append('사자')
print(animals)
print(animals[3])
print(animals[2])
del animals[2]  # 지우기
print(animals)
print(animals[0:2])  # Slicing도 가능
# list.sort()
animals.sort() # 가나다라 순 정리
print(animals)
animals.append('코알라')
#list.count() 값 개수
print(animals.count('코알라')) #코알라 수
print(animals.count('사자'))
del animals[1]
print(len(animals)) # len 은 리스트 값 수(내장함수)

#Tuple - 값 변경 못함 immutable != list , () 소괄호 사용 or not
my_tuple = ()
print(my_tuple)
print(type(my_tuple))
my_tuple = (1, 2, 3)
print(my_tuple)

#packing unpacking
my_tuple = 1, 2, 3 #packing
num1, num2, num3 = my_tuple
print(num1) #unpacking
num1 = 1
num2 = 2
print(num2)
num1, num2 = num2, num1 # num1=2 num2=1 로 바꿈
print(num1)
