import pandas as pd 
import streamlit as st 
import datetime as dt 


df = pd.read_excel('data_store_my_pham.xlsx', sheet_name='DonHang')

# Lọc theo cửa hàng
cua_hang = st.selectbox('**Lọc theo cửa hàng**',
                        [
                         'CH001','CH002', 'CH003', 'CH004','CH005'  
                        ]
                        )

# Lọc theo giời gian
thoi_gian = st.date_input('**Lọc theo thời gian**', value=(
    dt.date(2020, 1, 1) , dt.date(2025, 12, 31) 
))

start_date, end_date = thoi_gian
df['Ngay'] = pd.to_datetime(df['Ngay'])


# Lọc theo khoảng tiền thanh toán

min_value = st.number_input('Số tiền tối thiểu', min_value=0, value=0)
max_value = st.number_input('Số tiền tối đa', min_value=0, value=1000000)

df_filtered = df[
    (df['MaCuaHang'] ==cua_hang) &
    (df['Ngay'] >= pd.to_datetime(start_date)) &
    (df['Ngay'] <= pd.to_datetime(end_date)) &
    (df['TongTien']>=min_value) & 
    (df['TongTien']<=max_value)
]

df_all = pd.DataFrame()
df_all[['DonHang','TongTien']]= df_filtered[['MaDH','TongTien']]


st.dataframe(df_all)
st.write(f'Danh sách đơn hàng: {df_all.shape[0]}')
st.write(f"Tổng số tiền: {df_all['TongTien'].sum()}")


