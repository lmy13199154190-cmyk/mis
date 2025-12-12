import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

def generate_weekly_report(df_orders, df_risk, save_path="weekly_report.pdf"):

    # ---- 1. 生成统计图 ----
    plt.figure(figsize=(6,4))
    df_orders["day"] = pd.to_datetime(df_orders["order_time"]).dt.day
    df_orders.groupby("day").size().plot(kind="bar")
    plt.title("每日订单量")
    plt.xlabel("日期")
    plt.ylabel("订单数")
    plt.tight_layout()
    plt.savefig("orders.png")

    plt.figure(figsize=(6,4))
    df_risk.groupby("day")["risk_score"].mean().plot()
    plt.title("每日平均风险值")
    plt.tight_layout()
    plt.savefig("risk.png")

    # ---- 2. PDF ----
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Anpick — 安全外卖管理系统 周报", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"日期：{datetime.now().strftime('%Y-%m-%d')}", ln=True)

    pdf.ln(5)
    pdf.image("orders.png", w=180)
    pdf.ln(10)
    pdf.image("risk.png", w=180)

    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10,
    txt="本周总结：\n- 外卖投递稳定\n- 风险事件已降低\n- 高峰期提醒有效"
    )

    pdf.output(save_path)

    return save_path
