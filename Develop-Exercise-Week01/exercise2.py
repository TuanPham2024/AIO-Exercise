# 2. Viết function mô phỏng theo 3 activation function.
# Input:
# – Người dùng nhập giá trị x
# – Người dùng nhập tên activation function chỉ có 3 loại (sigmoid, relu, elu)

# Output: Kết quả f(x) (x khi đi qua activation function tương ứng theo activation function name).

# Ví dụ: Input: x=3, activation_function = 'relu' ->
#        Output: print 'relu: f(3)=3'

import math

def is_number(x):
  try :
    float(x) # Type - casting the string to 'float'.
  except ValueError : # If string is not a valid ‘float ‘,  it ’ll raise ‘ValueError ‘ exception
    return False
  return True

def sigmoid(x): return 1/(1+math.exp(-x))

def relu(x): return max(0,x)

def elu(x, alpha):
  if x <= 0:
    return alpha * (math.exp(x)-1)
  else:
    return x

def calc_activation_func(x, act_name):
  if(act_name == "sigmoid"):
    print(f"sigmoid: f({x}) = {sigmoid(x)}")
    return sigmoid(x)
  elif(act_name == "relu"):
      print(f"relu: f({x}) = {relu(x)}")
      return relu(x)
  elif(act_name == "elu"):
      alpha = float(input("Input float alpha = "))
      print(f"elu: f({x}) = {elu(x, alpha)}")
      return elu(x,alpha)


def exercise2():
  # Người dùng nhập giá trị x
  x = input("Input x = ")
  if not is_number(x):
    print("x must be number!")
    return
  else:
    x = float(x)

  # Người dùng nhập tên activation function chỉ có 3 loại (sigmoid, relu, elu)
  name_functions = ["sigmoid", "relu", "elu"]
  name_function = str(input("Input string activation Function ( sigmoid | relu |elu ):  "))

  if name_function not in name_functions:
    print(name_function + " is not supportted!")
    return
  else:
    calc_activation_func(x, name_function)

# SAMPLE -> KIEM TRA DU LIEU
#if __name__ == "_main__":  
exercise2()
