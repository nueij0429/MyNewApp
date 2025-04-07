#질문: 입력된 이메일 주소가 유효한지 검사하세요. (조건: @와 . 포함)

email = "user@example.com"
if "@" in email and "." in email:
    print("유효한 주소:", email)
else:
    print("유효하지 않은 주소")
