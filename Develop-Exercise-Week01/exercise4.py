# 4. Viết 4 functions để ước lượng các hàm số sau
# • Input: x (số muốn tính toán) và n (số lần lặp muốn xấp xỉ)
# • Output: Kết quả ước lượng hàm tương ứng với x. Ví dụ hàm cos(x=0) thì output = 1

# NOTE: Các bạn chú ý các điều kiện sau
# • x là radian
# • n là số nguyên dương > 0
# • các bạn nên viết một hàm tính giai thừa riêng

import math

# Hàm đệ quy
def factorial(n): #
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)

# print(factorial(4))

def approx_sin(x, n):
  total = 0
  for i in range(n):
    total += (-1)**i * (x**(2*i+1)) / factorial(2*i+1)
  return total

def approx_cos(x, n):
  total = 0
  for i in range(n):
    total += (-1)**i * (x**(2*i)) / factorial(2*i)
  return total

def approx_tan(x, n):
  total = 0
  for i in range(n):
    total += (-1)**i * (x**(2*i+1)) / factorial(2*i+1)
  return total

def approx_cot(x, n):
  total = 0
  for i in range(n):
    total += (-1)**i * (x**(2*i)) / factorial(2*i)
  return total    

def approx_sinh(x, n):
  total = 0
  for i in range(n):
    total += (x**(2*i+1)) / factorial(2*i+1)
  return total

def approx_cosh(x, n):
  total = 0
  for i in range(n):
    total += (x**(2*i)) / factorial(2*i)
  return total

def exercise4():
  print(approx_sin(x =3.14 , n =10))
  print(approx_cos(x =3.14 , n =10))
  print(approx_sinh(x=3.14 , n =10))
  print(approx_cosh(x=3.14 , n =10))
  print(approx_tan(x=3.14 , n =10))
  print(approx_cot(x=3.14 , n =10))
  return

# ____TEST____#
exercise4()