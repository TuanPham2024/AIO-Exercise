# Câu hỏi 1. Hoàn thành chương trình sau với mô tả bài toán từ câu I.1. Đầu ra của chương trình dưới đây là gì?
#def max(list_num): # buildin max bị báo lỗi do cach colab
#  max_value = list_num[0]
#  for i in list_num :
#    if i > max_value :
#      max_value = i
#  return max_value

def max_kernel(num_list , k):
  result = []
  for i in range(len(num_list) - k + 1):
    list_window = num_list[i:i+k]
    max_value = max(list_window) 
    result.append(max_value)  # print (num_list[i: i+k])
  return result

# TEST
assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5, 5, 5]

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] # hỏi gì
k = 3
print (max_kernel( num_list , k))