import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
#khoi tao bien
if "function_global" not in st.session_state:
        st.session_state.function_global = 0

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Tiêu đề ở giữa
st.markdown("<h1 class='centered-title'>VTI MOCK</h1>", unsafe_allow_html=True)
# Sử dụng st.columns để tạo hai cột
left_column, right_column = st.columns(2)


with left_column:
    rows1 = st.text_input("Nhập kích thước ma trận A",key ="row1_A_key")
    matrix1 = []
   
    rows2 = st.number_input("Nhập giá trị 1-1",key ="row2_A_key", min_value=1, value=2)

    matrix1.append(rows2)
    rows3 = st.number_input("Nhập giá trị 1-2",key ="row3_A_key", min_value=1, value=2)
    matrix1.append(rows3)
    print("Matrix 1:",matrix1)
    df = pd.DataFrame([
        {rows2,rows3}
    ])
    edited_df = st.data_editor(df, num_rows="dynamic")
    
    
with right_column:
   
    rows1 = st.text_input("Nhập kích thước ma trận B",key ="row1_B_key")
    matrix2 = []
    row_matrix_1 =[]
    row_matrix_2 = []
   
    rows2 = st.number_input("Nhập giá trị 1-1",key ="row2_B_key", min_value=1, value=2)
    row_matrix_1.append(rows2)
   
    rows3 = st.number_input("Nhập giá trị 1-2",key ="row3_B_key", min_value=1, value=2)
    row_matrix_1.append(rows3)
   
    rows4 = st.number_input("Nhập giá trị 2-1",key ="row2_4_key", min_value=1, value=2)
    row_matrix_2.append(rows4)
   
    rows5 = st.number_input("Nhập giá trị 2-2",key ="row3_5_key", min_value=1, value=2)
    row_matrix_2.append(rows5)

    matrix2.append(row_matrix_1)
    matrix2.append(row_matrix_2)

    print("Matrix 2:",matrix2)
    df = pd.DataFrame([
        {rows2,rows3},
        {rows4,rows5}
    ])
    edited_df = st.data_editor(df,key="edited_key", num_rows="dynamic")
# Trong cột bên trái, hiển thị đoạn văn bất kì
with st.sidebar:
    st.title("FUNCTION")
    

    if st.button("Cộng"):
        st.session_state.function_global = 1
        

    # print("Cong ban dau:", cong)
    if st.button("Trừ"):
        st.session_state.function_global = 2
    if st.button("Nhân"):
        st.session_state.function_global = 3
    if st.button("Chia"):
        st.session_state.function_global = 4
    print("Function global:",st.session_state.function_global)
    gpu = st.checkbox("Sử dụng GPU")
    button_result = st.button("Kết quả")
    if button_result:
        if gpu:
            with tf.device("/GPU:0"):  # Sử dụng GPU nếu có
                st.write("Kết quả sử dụng GPU")
                mat1 = tf.constant(matrix1, dtype=tf.float32)
                mat2 = tf.constant(matrix2, dtype=tf.float32)
                print("mat1 gpu:", mat1)
                print("mat2 gpu:", mat2)
                # print("Cong:", cong)
                if st.session_state.function_global == 1:
                    
                    result = tf.add(mat1, mat2)

                elif st.session_state.function_global == 2:
                    result = tf.subtract(mat1, mat2)
                    
                elif st.session_state.function_global == 3:
                    result = tf.matmul(mat1, mat2)
                   
                elif st.session_state.function_global == 4:
                    result = tf.divide(mat1, mat2)
                
                st.write(result.numpy())
                   
                
        else:
            st.write("Kết quả không sử dụng GPU")
            mat1 = np.array(matrix1)
            mat2 = np.array(matrix2)
            print("mat1 cpu:", mat1)
            print("mat2 cpu:", mat2)
            if st.session_state.function_global == 1:
                result = mat1 + mat2

            elif st.session_state.function_global == 2:
                result = mat1 - mat2
                
            elif st.session_state.function_global == 3:
                result = np.dot(mat1, mat2)
                
            elif st.session_state.function_global == 4:
                result = mat1 / mat2

            st.write(result)
            
    else:
        st.write("")




        





            
