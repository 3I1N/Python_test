#for 변수 in 컨테이너 :
#    실행할 명령 1 2 3 ...
animals = ['땅다람쥐', '사자', '호랑이']
for animal in animals:
    print(animal)
for num in [1, 2, 3]:
    print(num)
for my_str in "김왼손의 왼손코딩":
    print(my_str)

#range()
range(3)
print(range(3))
print(type(range(3)))

for n in [0, 1, 2]:
    print(n)
for n in range(0, 3): #0~2 까지 라는 의미
    print(n)
for n in range(0, 101):
    print(n)
range(3) #0~2까지
range(3, 5) #3,4

# forx2 (중복)
for n in range(5):
    print(n)
for j in range(2, 10):
    for i in range(1, 10):
        print('{} x {} = {}'.format(j, i, j*i)) # 구구단

#comprehension
numbers = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
odd_numbers = []

for number in numbers :
    if number % 2 == 1: # 2로 나누었을때 나머지 1인가
        odd_numbers.append(number)
print(odd_numbers)

print([number for number in numbers if number % 2 ==1]) #comprehension

#operator 연산자
# assign 할당연산자
# a = b , b를 a에 할당 (not same)
count = 0
print(count)
count = 1
print(count)
count = count + 1
print(count)
count += 1 # count = count + 1 와 같다 복합할당 연산자
print(count)
count -= 1
print(count)
# *=, /= 곱셉 나눗셈도 가능

#산술연산자 Arithmetic 31강 시작 해야함



