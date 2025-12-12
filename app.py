# app.py
import streamlit as st
from utils.db import init_db, query
from utils.auth import current_user, logout_user
import pages.login_page as login_page
import pages.register_page as register_page
import pages.dashboard as dashboard
import pages.orders as orders_page
import pages.risk_page as risk_page
import pages.config_page as config_page

st.set_page_config(page_title="AnPick MIS", layout="wide")

# initialize DB
con = init_db()

if "page" not in st.session_state:
    st.session_state["page"] = "login"

# sidebar navigation
st.sidebar.title("AnPick 管理系统")
user = current_user()

if not user:
    if st.session_state["page"] == "login":
        login_page.show(con)
    elif st.session_state["page"] == "register":
        register_page.show(con)
else:
    st.sidebar.markdown(f"**已登录：** {user['username']}  \n**角色：** {user['role']}")
    menu = st.sidebar.selectbox("导航", ["仪表盘","订单管理","风险监控","系统配置","登出"])
    if menu == "仪表盘":
        dashboard.show(con)
    elif menu == "订单管理":
        orders_page.show(con)
    elif menu == "风险监控":
        risk_page.show(con)
    elif menu == "系统配置":
        config_page.show(con)
    elif menu == "登出":
        logout_user()
        st.rerun()

#trigger rebuild
#second rebuild
#rebuild_2



