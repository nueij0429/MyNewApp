#질문: 12345초를 시간, 분, 초로 변환하세요.

seconds = 12345
h = seconds // 3600
m = (seconds % 3600) // 60
s = seconds % 60

print(f"{h}시간 {m}분 {s}초입니다.")
