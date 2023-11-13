import yfinance as yf
import plotly.graph_objects as go

# Ticker symbol của công ty (ví dụ: Apple)
ticker = "AAPL"

# Tải dữ liệu từ Yahoo Finance
data = yf.download(ticker, start="2022-01-01", end="2023-11-11")

# Tạo biểu đồ giá đóng cửa hàng ngày bằng plotly.graph_objects
fig = go.Figure()

fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=f'{ticker} Stock Price'))

fig.update_layout(
    title=f'{ticker} Stock Price Over Time',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Stock Price (USD)'),
    showlegend=True
)

fig.show()
