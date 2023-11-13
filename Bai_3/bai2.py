
"""
1. Tạo web bằng streamlit, tensorflow . Có chức năng : cộng trừ nhằn chia ma trận
    - Nhập vào kích thước ma trận 1 ,2 
    - Nhập vào ma trận 1,2 
    - 4 Button : Cộng, Trừ, Nhân , Chia 
    - 1 Button : Sử dụng GPU để tính toán 
    - Hiển thị ma trận kết quả 
"""
import streamlit as st
import tensorflow as tf

# Tiêu đề ứng dụng
st.title("Ứng dụng TensorFlow với Streamlit")

# Nhập kích thước ma trận 1
st.header("Nhập kích thước ma trận 1")
rows1 = st.number_input("Số hàng:", min_value=1, value=2)
cols1 = st.number_input("Số cột:", min_value=1, value=2)

# Nhập kích thước ma trận 2
st.header("Nhập kích thước ma trận 2")
rows2 = st.number_input("Số hàng:",key="rows2_key", min_value=1, value=2)
cols2 = st.number_input("Số cột:",key="cols2_key",min_value=1, value=2)

# Nhập ma trận 1
st.header("Nhập ma trận 1")
matrix1 = []
for i in range(rows1):
    row = []
    for j in range(cols1):
        key = f"value_cols1_{i}_{j}"  # Tạo một khóa duy nhất
        value = st.number_input(f"Giá trị hàng {i + 1}, cột {j + 1}:", step=0.01, key=key)
        row.append(value)
    matrix1.append(row)

# Nhập ma trận 2
st.header("Nhập ma trận 2")
matrix2 = []
for i in range(rows2):
    row = []
    for j in range(cols2):
        value = st.number_input(f"Giá trị hàng {i + 1}, cột {j + 1}:", step=0.01)
        row.append(value)
    matrix2.append(row)

# Chọn phép toán
operation = st.selectbox("Chọn phép toán:", ["Cộng", "Trừ", "Nhân", "Chia"])

# Sử dụng GPU để tính toán
if st.button("Sử dụng GPU để tính toán"):
    with tf.device("/GPU:0"):  # Sử dụng GPU nếu có
        mat1 = tf.constant(matrix1, dtype=tf.float32)
        mat2 = tf.constant(matrix2, dtype=tf.float32)
        if operation == "Cộng":
            result = tf.add(mat1, mat2)
        elif operation == "Trừ":
            result = tf.subtract(mat1, mat2)
        elif operation == "Nhân":
            result = tf.matmul(mat1, mat2)
        elif operation == "Chia":
            result = tf.divide(mat1, mat2)

        st.header("Ma trận kết quả")
        st.write(result.numpy())

    st.success("Tính toán hoàn tất trên GPU.")
