from utils.report import generate_weekly_report
import streamlit as st
import pandas as pd

def show(conn):
    st.title("📊 数据可视化与周报导出")

    orders = pd.read_sql("SELECT * FROM orders", conn)
    risks = orders[["order_time","risk_score"]].copy()

    if st.button("📄 生成本周 PDF 周报"):
        path = generate_weekly_report(orders, risks)
        with open(path, "rb") as f:
            st.download_button(label="下载周报 PDF",
                               data=f,
                               file_name="weekly_report.pdf",
                               mime="application/pdf")
