# 5. Viết function thực hiện Mean Difference of nth Root Error
# • Input: y (giá trị của y), y_hat (gía trị của yˆ), n (căn bậc n), và p (bậc của hàm loss)
# • Output: Kết quả của hàm loss
# Các bạn đọc thêm về hàm loss của yolo để thấy được ứng dụng
import math
import numpy as np


def different_n_root(y , y_hat, n, p) -> float:
  return (pow(y, 1/n) - pow(y_hat, 1/n))**p
   
def md_nre_single_sample(y , y_hat , n, p) -> float:
  """
  ## Parameter
    * y , y_hat , n, p: ...
  ## Return 
    return md_nre_single_sample
  """

  result = 0
  for _ in range(n):
    result += different_n_root(y, y_hat, n, p)
  result = (1/n)*result

  return result

print(md_nre_single_sample(y = 100 , y_hat = 99.5 , n = 2, p = 1))
print(md_nre_single_sample(y = 50  , y_hat = 49.5 , n = 2, p = 1))
print(md_nre_single_sample(y = 20  , y_hat = 19.5 , n = 2, p = 1))
print(md_nre_single_sample(y = 0.6 , y_hat = 0.1  , n = 2, p = 1))
