import streamlit as st

def menurender():
    st.sidebar.header("🔧 Điều hướng")
    st.sidebar.write("Chọn chức năng:")
    st.sidebar.page_link('pages/du_lieu.py', label = "Xem dữ liệu")
    st.sidebar.page_link('pages/don_hang.py', label = "Lọc đơn hàng")
    st.sidebar.page_link('pages/san_pham.py', label = "Thống kê sản phẩm")
    st.sidebar.page_link('pages/khach_hang.py', label = "Khách hàng")
    st.sidebar.page_link('pages/dashboard_don_gian.py', label = "Dashboard đơn giản")
    st.sidebar.markdown("---")
    st.sidebar.markdown("💡 Dành cho người mới bắt đầu <br>Pandas + Streamlit", unsafe_allow_html=True)    

    # page = st.sidebar.radio(
    #     "",
    #     (
    #         "Xem dữ liệu",
    #         "Lọc đơn hàng",
    #         "Thống kê sản phẩm",
    #         "Khách hàng",
    #         "Dashboard đơn giản"
    #     )
    # )

    

    # Điều hướng theo radio
    # if page == "Xem dữ liệu":
    #     st.switch_page("du_lieu")  # phải trùng tên file trong pages/ (không có .py)

    # elif page == "Lọc đơn hàng":
    #     st.switch_page("don_hang")

    # elif page == "Thống kê sản phẩm":
    #     st.switch_page("san_pham")

    # elif page == "Khách hàng":
    #     st.switch_page("khach_hang")

    # elif page == "Dashboard đơn giản":
    #     st.switch_page("dashboard_don_gian")
