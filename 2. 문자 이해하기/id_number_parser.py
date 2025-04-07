#질문: 주민등록번호 "901212-1234567"에서 생년월일을 추출하세요

id_number = "901212-1234567"
year = "19" + id_number[:2]
month = id_number[2:4]
day = id_number[4:6]

print(f"{year}년 {month}월 {day}일")