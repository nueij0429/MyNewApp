#["apple", "banana", "cherry"]에서 각 단어의 길이를 딕셔너리로 만드세요. 
# (딕셔너리 컴프리헨션 사용)

fruits = ["apple", "banana", "cherry"]
length_dict = {word: len(word) for word in fruits}

print(length_dict)