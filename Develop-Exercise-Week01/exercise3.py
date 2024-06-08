# 3. Viết function lựa chọn regression loss function để tính loss:
# • Input:
# – Người dùng nhập số lượng sample (num_samples) được tạo ra (chỉ nhận integer numbers)
# – Người dùng nhập loss name (MAE, MSE, RMSE-(optional)) chỉ cần MAE và MSE, bạn nào muốn làm thêm RMSE đều được.
#   -> calc_mae, calc_mse, calc_rmse

# • Output: Print ra loss name, sample, predict, target, loss
# – loss name: là loss mà người dùng chọn
# – sample: là thứ tự sample được tạo ra (ví dụ num_samples=5, thì sẽ có 5 samples
#           và mỗi sample là sample-0, sample-1, sample-2, sample-3, sample-4)
# – predict: là số mà model dự đoán (chỉ cần dùng random tạo random một số trong range [0,10))
# – target: là số target mà momg muốn mode dự đoán đúng (chỉ cần dùng random tạo random một số trong range [0,10))
# – loss: là kết quả khi đưa predict và target vào hàm loss
# – note: ví dụ num_sample = 5 thì sẽ có 5 cặp predict và target.

import random
import math

# Creat list_sample contain n_samples, with a sample = [predict, target] 
def creat_sample(num_samples):
  list_sample = []
  for i in range(num_samples):
    predict =  random.uniform(0, 10)  # uniform(start, end) -> random cho số nguyên
    target =  random.uniform(0, 10)
    list_sample.append([predict, target])
  return list_sample

# Calculate regression loss function
def calc_mae(list_sample):
  num_samples = len(list_sample)
  # total = 0
  # for i in range(num_samples): total += abs(list_sample[i][0] - list_sample[i][1])

  expresion_result = [abs(list_sample[i][0] - list_sample[i][1]) for i in range(num_samples)]
  total = sum(expresion_result)
  result = (1/num_samples)*total
  return result

def calc_mse(list_sample):
  num_samples = len(list_sample)
  #list_sample = creat_sample(num_samples)
  expresion_result = [(abs(list_sample[i][0] - list_sample[i][1]))**2 for i in range(num_samples)]
  result = (1/num_samples)*sum(expresion_result)
  return result

def calc_rmse(list_sample):
  result = math.sqrt(calc_mse(list_sample))
  return result




# Người dùng nhập số lượng sample -> int 


def exercise3():
  #1: Người dùng nhập num_samples type int
  num_samples = input("Input num_samples = ") #input num
  
  if not num_samples.isnumeric():
    print("num_samples must be int!")
    return
  else:
    num_samples = int(num_samples)

  # try:   num_samples = int(input("Input num_samples = "))
  # except ValueError :  print("num_samples must be int!")
  #   # return

  if num_samples <= 0:
    print("num_samples must be greater than 0!")
    return

  #2. Người dùng nhập loss name (MAE, MSE, RMSE-(optional)
  list_lost_names = ["MAE", "MSE", "RMSE"]
  loss_name = str(input("Input string loss Function ( MAE | MSE | RMSE ):  "))
  if loss_name not in list_lost_names:
    print(loss_name + " is not supportted!")
    return
  #3: Tạo list_sample ngẫu nhiên và in ra
  list_sample = creat_sample(num_samples)

  #4: Tính toán loss tương tương ứng
  loss = 0.0
  if loss_name == list_lost_names[0]:
    loss = calc_mae(list_sample)
  elif loss_name == list_lost_names[1]:
    loss = calc_mse(list_sample)
  elif loss_name == list_lost_names[2]:
    loss = calc_rmse(list_sample)
  else:
    print("Error")
    return

  # Cuối cùng, in kiểm tra, num list list_sample
  print(f"Num_samples = {num_samples}.")
  print(f"List_sample = {list_sample}")
  print(f"Loss = {loss}")
  

# ____TEST____#
# print(calc_mae(5))
# print(calc_mse(5))
# print(calc_rmse(5))
# print(list_sample)
exercise3()
