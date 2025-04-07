#질문: 10000원을 3명이서 똑같이 나누어 가질 때 각자 얼마를 받고 얼마가 남는지 계산하세요.

money = 10000
each = money // 3
remain = money % 3

print(f"각자 {each}원을 받고 {remain}원이 남습니다.")
