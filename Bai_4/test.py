import streamlit as st

# Tạo một danh sách để lưu trữ các sự kiện
events = st.session_state.get("events", [])

# Button 1
if st.button("Button 1"):
    st.write("but 1")
    events.append("Sự kiện từ Button 1 đã xảy ra.")

# Button 2
if st.button("Button 2"):
    st.write("but 2")
    events.append("Sự kiện từ Button 2 đã xảy ra.")

# Lưu danh sách sự kiện vào biến trạng thái
st.session_state.events = events

# Hiển thị các sự kiện đã xảy ra
st.write("Các sự kiện đã xảy ra:")
if st.button("Button 3:"):
    for event in events:
        st.write(event)
