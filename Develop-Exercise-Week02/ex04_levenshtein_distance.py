# Câu hỏi 4:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.4. Đầu ra của chương trình dưới đây là gì?
# ''' Khoảng cách Levenshtein thể hiện khoảng cách khác biệt giữa 2 chuỗi ký tự.
# Khoảng cách Levenshtein giữa chuỗi S và chuỗi T là số bước ít nhất biến chuỗi S thành chuỗi T
# thông qua 3 phép biến đổi là:
# • Xoá một ký tự
# • Thêm một ký tự
# • Thay thế ký tự này bằng ký tự khác
# Khoảng cách này được sử dụng trong việc tính toán sự giống và khác nhau giữa 2 chuỗi, như chương trình kiểm tra lỗi chính tả của winword spellchecker? '''

import numpy as np

# Khoảng cách Levenshtein giữa chuỗi S và chuỗi T
def levenshtein_distance(source, target):
    rows = len(source) + 1
    cols = len(target) + 1
    l_matrix = np.zeros((rows, cols)) # 1 create the matrix
  
    l_matrix[0, :] = range(cols) # 2 fill the 1st row
    l_matrix[:, 0] = range(rows) # 2 fill the 1st column

    # calculate associated cost
    def del_cost():
        return 1

    def ins_cost():
        return 1

    def sub_cost(source, target):
        return 0 if source == target else 1

    # 3 fill the remaining cells
    for i in range(1, rows):
        for j in range(1, cols):
            del_ = l_matrix[i-1, j] + del_cost()
            ins_ = l_matrix[i, j-1] + ins_cost()
            sub_ = l_matrix[i-1, j-1] + sub_cost(source[i-1], target[j-1])

            l_matrix[i, j] = min(del_, ins_, sub_)

    return l_matrix[rows-1, cols-1]

# MC4
print(f"levenshtein_distance('hola','hello') = {levenshtein_distance('hola', 'hello')} - Answer: c)")