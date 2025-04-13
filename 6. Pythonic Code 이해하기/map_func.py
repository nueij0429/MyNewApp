#두 리스트 [1, 2, 3]과 [4, 5, 6]의 각 요소를 더한 새 리스트를 생성하세요. 
# (map 함수 사용)

a = [1, 2, 3]
b = [4, 5, 6]

added = list(map(lambda x, y: x + y, a, b))

print(added)