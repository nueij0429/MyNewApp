#질문: "Python is awesome"에서 모음(a, e, i, o, u)의 개수를 세세요.

text = "Python is awesome"
count = sum(1 for c in text.lower() if c in "aeiou")

print("모음 개수:", count)
