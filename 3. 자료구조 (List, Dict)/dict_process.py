#질문: {"name": "John", "age": 30} 딕셔너리에서 "age"의 값을 출력하세요.
# {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명을 출력하세요.
# 딕셔너리 {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키세요.
# [5, 2, 8, 1, 9] 리스트를 오름차순으로 정렬하세요.


person = {"name": "John", "age": 30}
print("나이:", person["age"])

scores = {"math": 90, "science": 85, "history": 78}
print(list(scores.keys()))

fruits = {"apple": 3, "banana": 5}
fruits["apple"] += 2
print(fruits)

nums = [5, 2, 8, 1, 9]
nums.sort()
print(nums)
