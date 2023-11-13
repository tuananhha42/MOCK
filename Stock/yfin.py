import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
from datetime import date
import pickle
import matplotlib.pyplot as plt

# Định nghĩa CSS trực tiếp bằng cách sử dụng st.markdown
st.markdown(
    """
    <style>
    .red-text {
        color: red;
        font-size: 30px;  /* Thay đổi cỡ chữ thành 30px */
    }
    </style>

    <style>
    .edit-text_yellow {
        color: #D4F005;
        font-size: 16px;  /* Thay đổi cỡ chữ thành 18px */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Thông tin giao dịch chứng khoán")
# Tạo ứng dụng Streamlit
st.sidebar.title('Nhập dữ liệu chứng khoán')

# Tạo một từ điển ánh xạ tên công ty thành mã công ty
company_codes = {
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Google": "GOOGL",
    "Microsoft": "MSFT",
    "Meta": "META"
}
# Danh sách các công ty
companies = list(company_codes.keys())
# Tạo select box cho việc chọn công ty
selected_company = st.sidebar.selectbox("Chọn một công ty:", companies)
# Lấy mã công ty tương ứng với công ty đã chọn
selected_company_code = company_codes[selected_company]


selected_date_start = st.sidebar.date_input("Chọn ngày bắt đầu", date.today(), key = 'selected_date_start')
# Hiển thị ngày đã chọn
st.sidebar.write("Ngày bắt đầu:", selected_date_start)

selected_date_end = st.sidebar.date_input("Chọn ngày kết thúc", date.today(),key = 'selected_date_end')
# Hiển thị ngày đã chọn
st.sidebar.write("Ngày kết thúc:", selected_date_end)

if st.sidebar.button('Xem thông tin dữ liệu'):
    # Sử dụng Yahoo Finance để lấy dữ liệu chứng khoán
    try:
        df = yf.download(selected_company_code, start=selected_date_start, end=selected_date_end)
        
        # Hiển thị dữ liệu chứng khoán
        st.write('Dữ liệu chứng khoán:')
        st.write(df)

        # Vẽ biểu đồ giá đóng cửa hàng ngày
        st.write('Biểu đồ giá đóng cửa hàng ngày:')
        fig = go.Figure(data=go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']))
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Không thể lấy dữ liệu chứng khoán cho {selected_company_code}: {e}")

# Đọc các mô hình huấn luyện
model_Apple = pickle.load(open('Model_data/Apple.pkl', 'rb'))
model_Amazon = pickle.load(open('Model_data/Amazon.pkl', 'rb'))
model_Meta = pickle.load(open('Model_data/Meta.pkl', 'rb'))
model_Google = pickle.load(open('Model_data/Google.pkl', 'rb'))
model_Microsoft = pickle.load(open('Model_data/Microsoft.pkl', 'rb'))

# Đọc các mô hình chuẩn hóa
Scale_Apple = pickle.load(open('Scaler_data/Scaler_Apple.pkl', 'rb'))
Scale_Amazon = pickle.load(open('Scaler_data/Scaler_Amazon.pkl', 'rb'))
Scale_Meta = pickle.load(open('Scaler_data/Scaler_Meta.pkl', 'rb'))
Scale_Google = pickle.load(open('Scaler_data/Scaler_Google.pkl', 'rb'))
Scale_Microsoft = pickle.load(open('Scaler_data/Scaler_Microsoft.pkl', 'rb'))

# Tiện ích nhập liệu cho thông tin giao dịch
st.sidebar.title('Nhập thông tin giao dịch:')
open_price = st.sidebar.number_input("Open", min_value=0.0, key='open_price')
high_price = st.sidebar.number_input("High", min_value=0.0, key='high_price')
low_price = st.sidebar.number_input("Low", min_value=0.0, key='low_price')
close_price = st.sidebar.number_input("Close", min_value=0.0, key='close_price')
volume = st.sidebar.number_input("Volume", min_value=0, key='volume')

if st.sidebar.button("Xem thông tin mô hình huấn luyện"):
    # Tạo từ điển ánh xạ mã công ty vào mô hình dự đoán và chuẩn hóa tương ứng
    model_mapping = {
        "AAPL": (model_Apple, Scale_Apple),
        "AMZN": (model_Amazon, Scale_Amazon),
        "META": (model_Meta, Scale_Meta),
        "GOOGL": (model_Google, Scale_Google),
        "MSFT": (model_Microsoft, Scale_Microsoft)
    }

    # Lấy mô hình và chuẩn hóa tương ứng với mã công ty đã chọn
    selected_model, selected_scaler = model_mapping.get(selected_company_code, (None, None))

    if selected_model is not None:
        st.write(f"Mã công ty: {selected_company_code}")
        st.write(f"Mô hình dự đoán: {selected_model}")
        st.write(f"Mô hình chuẩn hóa: {selected_scaler}")
    else:
        st.write("Không có mô hình dự đoán và mô hình chuẩn hóa tương ứng với công ty đã chọn.")


#Tạo 1 list để lưu dữ liệu dự đoán sau mỗi lần ấn nút predict bằng session state
if "predicted_prices" not in st.session_state:
    st.session_state.predicted_prices = []

# Hàm dự đoán giá cổ phiếu
def predict_stock_price(open_price, high_price, low_price, close_price, volume, selected_company_code):
    if selected_company_code == 'AAPL':
        model = model_Apple
        scaler = Scale_Apple
    elif selected_company_code == 'AMZN':
        model = model_Amazon
        scaler = Scale_Amazon
    elif selected_company_code == 'META':
        model = model_Meta
        scaler = Scale_Meta
    elif selected_company_code == 'GOOGL':
        model = model_Google
        scaler = Scale_Google
    elif selected_company_code == 'MSFT':
        model = model_Microsoft
        scaler = Scale_Microsoft
    # Chuẩn hóa dữ liệu đầu vào
    input_data = scaler.transform([[open_price, high_price, low_price, close_price, volume]])
    
    # Dự đoán giá cổ phiếu
    predicted_price = model.predict(input_data)
    
    return predicted_price[0]

if st.sidebar.button("Dự báo"):
    predicted_price = predict_stock_price(open_price, high_price, low_price, close_price, volume, selected_company_code)
    st.session_state.predicted_prices.append(predicted_price)
    st.markdown(f'<p class="red-text">Dự đoán giá cổ phiếu: ${(predicted_price):,.2f}</p>', unsafe_allow_html=True) # sử dụng markdown đã đc tạo từ trc

    # Hiển thị danh sách giá dự đoán từ các lần nhấn trước đó
    if st.session_state.predicted_prices:
        st.write("Danh sách giá dự đoán từ các lần nhấn trước đó:")
        for i, price in enumerate(st.session_state.predicted_prices):
            st.markdown(f'<p class="edit-text_yellow">Dự đoán {i + 1}: ${price:,.2f}</p>', unsafe_allow_html=True)
    
   # Vẽ biểu đồ đường
    plt.figure(figsize=(10, 6), facecolor='black')
    plt.plot(range(1, len(st.session_state.predicted_prices) + 1), st.session_state.predicted_prices, color='lime')
    plt.xlabel('Prediction Number', color='white', fontsize=12)
    plt.ylabel('Predicted Price', color='white', fontsize=12)
    plt.title('Biểu đồ giá dự đoán', color='white', fontsize=14)
    plt.gca().set_facecolor('black')
    plt.tick_params(axis='x', colors='white', labelsize=10)
    plt.tick_params(axis='y', colors='white', labelsize=10)
    st.pyplot(plt)

if st.sidebar.button('Reset'):
    # Đặt lại tất cả các giá trị về giá trị mặc định
    open_price = 0.0
    high_price = 0.0
    low_price = 0
    close_price = 0
    volume = 0
    # Xóa danh sách predicted_prices
    st.session_state.predicted_prices = []