# Câu hỏi 3: Hoàn thành chương trình sau với mô tả bài toán từ câu I.3. Đầu ra của chương trình dưới đây là gì?

### DOWNLOAD FILE = TU GG File ###
# If you are using google-colab, try:   
#     !pip install --upgrade --no-cache-dir gdown
#     !gdown --id [id of your file]

import re
url = 'https://drive.google.com/file/d/1IBScGdW2xlNsc9v5zSAya548kNgiOrko/view'
def extract_file_id(url) -> str:
    """
    ## Parameter
    url: Link ggoog drive
    -----------------------
    ## Return
    Return string file id between /d/ and /view
    """
    match = re.search(r'/file/d/([a-zA-Z0-9_-]+)/view', url)
    if match:
        return match.group(1)  # Trả về ID nếu tìm thấy
    return ""  # Trả về None nếu không tìm thấy ID //None

file_id = extract_file_id(url)#'1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
#!gdown https://drive.google.com/uc?id=$file_id # chãy trên coblab


# In my case, I ran the following command and try using gdown, and problem was solved:  (pip install --upgrade --no-cache-dir gdown ->TEST)
# GOOD: 
#1. pip install gdown   # Cài dặt gdown
#2. pip show gdown      # Kiểm tra
#3. gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko  # Thử lệnh gốc
#4. Sử dụng trực tiếp trong code pyhton:
#   url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
#   output = 'tênfileLuuVe.txt'  # Tên tệp bạn muốn lưu
#   gdown.download(url, output, quiet=False)
# Tải tệp



#### CODE lỗi không hiểu lí do -> Khắc phục sau ###-----------------------------------------

#Code doi chinh sửa: import gdown 
#output_folder = 'E:\2024_AIO_VN\2024_AIO_MAIN\AIO-236-Excersice\AIO-Exercise'#'path/to/your/folder'
#output_filename = 'P1_data.txt'  # Tên tệp mà bạn muốn lưu + đường dẫn. Default = thư mục hiện tại với tên đã chỉ định
#output = output_folder + '\\' + output_filename # output = os.path.join(output_folder, 'downloaded_file.ext')

## Tạo thư mục nếu chưa tồn tại
#import os
#if not os.path.exists(output_folder):
#    os.makedirs(output_folder)

## Tải tệp
#gdown.download(url, output, quiet=False)

#### CODE lỗi không hiểu lí do -> Khắc phục sau ###


def count_word(file_path) -> dict:
  counter = {}
  # Your Code Here
  with open(file_path, 'r') as f: # read the file
      content = f.read() # content = string of file
      words = content.strip().split() # create word list from file content
      for word in words:    # turn all word to lower case, and count , return to dict
        counter[word] = counter.get(word.lower(), 0) + 1
  return counter

file_path = '/content/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])