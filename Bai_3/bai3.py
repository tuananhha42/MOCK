"""
2. Tạo web bằng streamlit, cv2 . Có chức năng : Xử lí hỉnh ảnh 

    - Nhập vào 1 hình ảnh
    - Hiển thị hình ảnh
    - 5 button với chức năng chỉnh sửa hỉnh ảnh : 
        + Xoay ảnh : -180 -> 180 độ 
        + Chỉnh đậm nhạt
        + Lọc màu : anh, đỏ , ghi 
        + Crop ảnh 
    - Hiền thị hình ảnh sau khi chỉnh sửa
"""
import streamlit as st
import cv2
import numpy as np

# Tiêu đề ứng dụng
st.title("Ứng dụng xử lý hình ảnh với Streamlit và OpenCV")

# Nhập hình ảnh từ người dùng
st.header("Nhập hình ảnh")
uploaded_image = st.file_uploader("Chọn một hình ảnh:", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Đọc hình ảnh từ tệp tải lên
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Hiển thị hình ảnh gốc
    st.image(image, caption="Hình ảnh gốc", use_column_width=True, channels="BGR")

    # Chọn chức năng chỉnh sửa hình ảnh
    st.subheader("Chọn chức năng chỉnh sửa hình ảnh:")
    edit_option = st.selectbox("Chọn chức năng:", ["Xoay ảnh", "Chỉnh đậm/nhạt", "Lọc màu", "Crop ảnh"])

    # Xử lý hình ảnh dựa trên lựa chọn
    if edit_option == "Xoay ảnh":
        # Góc xoay tùy chỉnh
        rotation_angle = st.slider("Góc xoay (độ):", -180, 180, 0)

        # Xử lý hình ảnh bằng cách xoay
        if rotation_angle != 0:
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, rotation_angle, 1.0)
            rotated_image = cv2.warpAffine(image, M, (w, h))
            st.image(rotated_image, caption="Hình ảnh sau khi xoay", use_column_width=True, channels="BGR")

    elif edit_option == "Chỉnh đậm/nhạt":
        alpha = st.slider("Độ đậm/nhạt:", 0.0, 2.0, 1.0)
        adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
        st.image(adjusted_image, caption="Hình ảnh chỉnh đậm/nhạt", use_column_width=True, channels="BGR")

    elif edit_option == "Lọc màu":
        color_filter = st.selectbox("Chọn màu:", ["None", "Xanh lá", "Đỏ", "Xám"])
        if color_filter == "Xanh lá":
            filtered_image = image.copy()
            filtered_image[:, :, 1] = 0  # Lọc chỉ màu xanh lá
            st.image(filtered_image, caption="Hình ảnh sau khi lọc màu", use_column_width=True, channels="BGR")
        elif color_filter == "Đỏ":
            filtered_image = image.copy()
            filtered_image[:, :, 0] = 0  # Lọc chỉ màu đỏ
            st.image(filtered_image, caption="Hình ảnh sau khi lọc màu", use_column_width=True, channels="BGR")
        elif color_filter == "Xám":
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            st.image(gray_image, caption="Hình ảnh sau khi chuyển thành ảnh xám", use_column_width=True, channels="GRAY")

    elif edit_option == "Crop ảnh":
        x1 = st.number_input("Tọa độ x1:", min_value=0, max_value=image.shape[1], value=0)
        y1 = st.number_input("Tọa độ y1:", min_value=0, max_value=image.shape[0], value=0)
        x2 = st.number_input("Tọa độ x2:", min_value=0, max_value=image.shape[1], value=image.shape[1])
        y2 = st.number_input("Tọa độ y2:", min_value=0, max_value=image.shape[0], value=image.shape[0])
        cropped_image = image[y1:y2, x1:x2]
        st.image(cropped_image, caption="Hình ảnh sau khi cắt", use_column_width=True, channels="BGR")
