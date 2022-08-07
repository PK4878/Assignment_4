def square_no(n):
  return n * n
nums = [4, 5, 2, 9]
result = map(square_no, nums)
print("Square the using map():")
print(list(result))