# 파이썬 연습

## for 문

- 반복문은 for 변수명 in (배열 or 함수)로 실행한다

```python
name = ["창현", "정", "민섭", "규석"]

for n in name:
    print(n)
```

## if 문

- 조건문은 if 조건, elif 조건, else 형태로 실행한다

```python
name = ["창현", "정", "민섭", "규석"]

for n in name:
    if n == "정":
        print(n)
    elif n == "규석":
        print(n + "은 바보")
    else:
        print("백수")
```