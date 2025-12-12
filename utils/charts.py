# utils/charts.py
import pandas as pd
import plotly.express as px
from dateutil import parser

def orders_df(rows):
    # rows: list of tuples from DB
    cols = ["id","order_id","user_id","courier_id","cabinet_id","order_time","delivery_time","in_cabinet_time","out_cabinet_time","status","risk_score","notes"]
    df = pd.DataFrame(rows, columns=cols)
    return df

def plot_risk_time_distribution(df):
    if df.empty:
        return None
    # convert times
    df["in_hour"] = df["in_cabinet_time"].apply(lambda x: parser.parse(x).hour if x else None)
    counts = df.groupby("in_hour").size().reset_index(name="count").dropna()
    fig = px.bar(counts, x="in_hour", y="count", labels={"in_hour":"Hour","count":"异常数"}, title="高风险时段分布")
    return fig

def plot_cabinet_heatmap(df):
    if df.empty:
        return None
    agg = df.groupby("cabinet_id")["risk_score"].sum().reset_index()
    fig = px.bar(agg, x="cabinet_id", y="risk_score", title="按柜子汇总的风险得分")
    return fig
