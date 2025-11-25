import streamlit as st 
import pandas as pd 

st.subheader("📋 Thống kê sản phẩm")

# Hiển thị danh sách tất cả sản phẩm
df = pd.read_excel('data_store_my_pham.xlsx', sheet_name='SanPham')
st.write('**📦 Danh sách tất cả sản phẩm**')
st.dataframe(df)
st.markdown('-----')

# Sản phẩm có giá cao nhất
df_gia_cao_nhat = df.nlargest(1, 'Gia')
st.write('**💰 Sản phẩm có giá cao nhất**', df_gia_cao_nhat)
st.markdown('-----')

# Sản phẩm có giá thấp nhất
df_gia_thap_nhat = df.nsmallest(1, 'Gia')
st.write('**🏷️ Sản phẩm có giá thấp nhất**', df_gia_thap_nhat)


# Giá trung bình của tất cả sản phẩm
df_gia_trung_binh = df['Gia'].mean()
st.write('**📈 Giá Trung Của Tất Cả Các Sản Phẩm**', df_gia_trung_binh)
st.markdown('----')
# Tổng số sản phẩm tồn kho
df_so_luong_ton = df['SoLuongTon'].sum()
st.write('**📦 Tổng số sản phẩm tồn kho**', df_so_luong_ton) 
