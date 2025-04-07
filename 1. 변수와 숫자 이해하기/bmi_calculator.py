#질문: 사용자로부터 체중(kg)과 키(cm)를 입력받아 BMI를 계산하세요.

total_seconds = 12345
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds}초는 {hours}시간 {minutes}분 {seconds}초입니다.")