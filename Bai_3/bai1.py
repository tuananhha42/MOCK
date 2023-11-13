import streamlit as st
"""
Bài tập 1: Tạo nút nhấn và hiển thị
        Tạo một ứng dụng Streamlit đơn giản với một nút nhấn.
        Khi người dùng nhấn nút, hiển thị một dòng chữ "Hello"
"""
st.title("Ứng dụng Streamlit với Button")
if st.button("Hay an vao day"):
    st.write('Hello')

"""
Bài tập 2: Sự kiện và cập nhật dữ liệu
        Tạo một ứng dụng với một ô văn bản và một nút nhấn.
        Khi người dùng nhập văn bản và nhấn nút, hiển thị thông điệp dựa trên văn bản họ đã nhập.
"""
# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit đơn giản")

# Thêm một ô văn bản cho người dùng nhập
user_input = st.text_input("Nhập văn bản:", "")

# Thêm một nút nhấn
if st.button("Hiển thị thông điệp"):
    st.write(f"Bạn đã nhập: {user_input}")

"""
Bài tập 3: Chia cột và hiển thị danh sách
        Tạo một ứng dụng với hai cột.
        Trong cột bên trái, hiện thị 1 đoạn văn bất kì
        Trong cột bên phải, hiện thị 1 đoạn văn bất kì
"""
# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit với hai cột")

# Sử dụng st.columns để tạo hai cột
left_column, right_column = st.columns(2)

# Trong cột bên trái, hiển thị đoạn văn bất kì
with left_column:
    st.write("Đoạn văn trong cột bên trái")
    st.write("Đây là một ví dụ về nội dung trong cột bên trái")

# Trong cột bên phải, hiển thị đoạn văn bất kì
with right_column:
    st.write("Đoạn văn trong cột bên phải")
    st.write("Đây là một ví dụ về nội dung trong cột bên phải")

"""
Bài tập 4: Tải lên tệp và hiển thị hình ảnh
        Tạo một ứng dụng cho phép người dùng tải lên một tệp hình ảnh.
        Khi họ tải lên, hiển thị hình ảnh trong ứng dụng.
"""
from PIL import Image
import io
# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit với tải lên hình ảnh")

# Sử dụng st.file_uploader để cho phép người dùng tải lên tệp hình ảnh
uploaded_image = st.file_uploader("Tải lên hình ảnh", type=["jpg", "png", "jpeg"])

# Kiểm tra xem người dùng đã tải lên hình ảnh chưa
if uploaded_image is not None:
    # Đọc hình ảnh từ tệp tải lên
    image = Image.open(uploaded_image)

    # Hiển thị hình ảnh trong ứng dụng
    st.image(image, caption="Hình ảnh tải lên", use_column_width=True)

"""
Bài tập 5: Chọn hình ảnh từ danh sách và hiển thị
        Tạo một ứng dụng với một danh sách các hình ảnh và một nút nhấn.
        Khi người dùng nhấn nút, hiển thị hình ảnh được chọn từ danh sách lên giao diện.
"""
st.title("Ứng dụng Streamlit với chọn hình ảnh")

# Danh sách các hình ảnh
image_list = {
    "Hình 1": "img1.jpg",
    "Hình 2": "img2.jpg",
    
}

# Sử dụng st.selectbox để cho phép người dùng chọn một hình ảnh từ danh sách
selected_image = st.selectbox("Chọn một hình ảnh:", list(image_list.keys()))

# Hiển thị hình ảnh được chọn khi người dùng nhấn nút
if st.button("Hiển thị hình ảnh"):
    image_path = image_list.get(selected_image)
    if image_path:
        st.image(image_path, caption=selected_image, use_column_width=True)
    else:
        st.warning("Hình ảnh không tồn tại.")