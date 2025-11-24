import streamlit as st 
import pandas as pd 
from menu import menurender 

st.set_page_config(layout='wide')
st.title('📊Ứng dung phân tích chuỗi cửa hàng mỹ phẩm LISASTORE')
st.header('📄Xem dữ liệu các bảng')

menurender() 
table = st.selectbox('Chọn bảng dữ liệu',
             ['CuaHang','NhanVien','KhachHang','SanPham','DonHang'])

# Bạn đang xem dữ liệu
st.write(f'**Bạn đang xem** {table}')  

# Đọc sheet theo lựa chọn      
df = pd.read_excel('data_store_my_pham.xlsx', sheet_name=table)
# Thông tin tổng quản
st.write(f'**Số dòng**: {df.shape[0]} |**Số cột**: {df.shape[1]}') 
# Hiển thị dữ liệu
st.dataframe(df)


