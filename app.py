import streamlit as st 
from menu import menurender 

st.set_page_config(layout='wide')
st.title('📊Ứng dung phân tích chuỗi cửa hàng mỹ phẩm LISASTORE')
st.header('📄Xem dữ liệu các bảng')

menurender() 


