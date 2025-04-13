#[10, 20, 30, 40, 50]에서 30보다 큰 수만 필터링하세요.

nums = [10, 20, 30, 40, 50]
filtered = list(filter(lambda x: x > 30, nums))

print(filtered)