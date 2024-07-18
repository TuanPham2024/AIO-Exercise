# pip install streamlit
# python.exe -m pip install --upgrade pip streamlit  #Update streamlit
# python -m streamlit run Develop-Exercise-Week04\Streamlit.py  #-> Chạy file streamlit "RelativePath_file.py"

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Các hàm hiển thị cơ bản:
st.title("Ứng dụng Streamlit đầu tiên của tôi")
st.header("Hiển thị đầu đề")
st.subheader("Hiển thị đầu đề phụ")
st.write("Xin chào, đây là một ứng dụng Streamlit đơn giản!")
st.text("Hiển thị văn bản thường")
st.markdown("Hiển thị văn bản định dạng Markdown")
st.code("""
if st.button("Nhấn vào tôi"):
    st.write("Bạn đã nhấn nút!")
        """)

# Các widget tương tác:
st.title("Ví dụ về các Widget tương tác trong Streamlit")
st.text("""
        st.text_input("Tạo ô nhập văn bản") \n
        st.button("Tạo nút") \n
        st.checkbox("Tạo hộp kiểm Hiện/Ẩn") \n
        st.radio("Tạo nút radio", ('Pop', 'Rock', 'Classical')) \n
        st.selectbox("Tạo hộp chọn",options = ('Đỏ', 'Xanh lá', 'Xanh dương')) \n
        st.slider("Tạo thanh trượt") 
          """)

# 1. Button
if st.button("Nhấn vào tôi"):
    st.write("Bạn đã nhấn nút!")

# 2. Checkbox
if st.checkbox("Hiển thị/Ẩn"):
    st.write("Bạn đã chọn hiển thị nội dung này.")

# 3. Radio button
genre = st.radio(
    "Thể loại âm nhạc yêu thích của bạn là gì?",
    ('Pop', 'Rock', 'Classical'))
st.write(f"Bạn đã chọn {genre}")

# 4. Selectbox
option = st.selectbox(
    'Màu sắc yêu thích của bạn là gì?',
    ('Đỏ', 'Xanh lá', 'Xanh dương'))
st.write(f'Bạn đã chọn: {option}')

# 4. multiselect
options = st.multiselect(" Your favorite colors :",
                         ["Green", "Yellow", "Red", "Blue"],  # options
                         ["Yellow", "Red"])  # Default options
st.write("You selected :", options)

# 5. Slider
age = st.slider('Bao nhiêu tuổi?', 0, 130, 25)
st.write(f"Tôi là: {age} tuổi")

# 6. Text input
name = st.text_input('Nhập tên của bạn')
if name:
    st.write(f'Xin chào {name}!')


# # Hiển thị dữ liệu:


# st.dataframe(): Hiển thị bảng dữ liệu
# st.table(): Hiển thị bảng tĩnh
# st.json(): Hiển thị dữ liệu JSON


# #Vẽ đồ thị:


# st.line_chart(): Vẽ biểu đồ đường
# st.bar_chart(): Vẽ biểu đồ cột
# st.pyplot(): Hiển thị đồ thị từ Matplotlib

# Hiển thị hình ảnh
st.image("Data\CAT.jpg", caption='A cat', width=100, channels='RGB')

# FORM tương tác
with st.form("FORM tương tác, my_form: "):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last  Name')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name : ", f_name,  " - Last Name : ", l_name)

    uploaded_files = st.file_uploader(
        "Choose files", accept_multiple_files=True)

# FILES - input
uploaded_files = st.file_uploader(
    "Choose mutil files", accept_multiple_files=True)


# Tạo dữ liệu mẫu
rng = np.random.default_rng(0)  # Sử dụng Generator thay vì seed dễ ảnh hưởng toàn cục vi phạm pep8
df = pd.DataFrame({
    'x': range(100),
    'y': rng.standard_normal(100).cumsum()
})

# Tạo layout với columns
left_column, right_column = st.columns(2)

# Left pane
with left_column:
    st.header("Cài đặt")

    # Slider để chọn số điểm dữ liệu
    num_points = st.slider("Số điểm dữ liệu", 10, 100, 50)

    # Radio button để chọn loại biểu đồ
    chart_type = st.radio("Chọn loại biểu đồ", ("Line", "Scatter", "Bar"))

# Right pane
with right_column:
    st.header("Biểu đồ")

    # Vẽ biểu đồ dựa trên lựa chọn của người dùng
    fig, ax = plt.subplots()

    if chart_type == "Line":
        ax.plot(df['x'][:num_points], df['y'][:num_points])
    elif chart_type == "Scatter":
        ax.scatter(df['x'][:num_points], df['y'][:num_points])
    else:  # Bar
        ax.bar(df['x'][:num_points], df['y'][:num_points])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'{chart_type} Chart')

    # Hiển thị biểu đồ trong Streamlit
    st.pyplot(fig)

# Hiển thị dữ liệu dưới dạng bảng
st.header("Dữ liệu")
st.dataframe(df.head(num_points))

# Sử dụng st.sidebar để tạo thanh bên
st.sidebar.header("Thông tin bổ sung")
st.sidebar.write(
    "Đây là một ví dụ về cách sử dụng left pane, right pane, và vẽ đồ thị trong Streamlit.")
st.sidebar.info(
    "Bạn có thể thay đổi số điểm dữ liệu và loại biểu đồ ở cột bên trái.")
