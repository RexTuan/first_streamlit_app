##[memo]
"""
streamlit檔案只要存檔, 會實時同步至網頁中!
"""

import streamlit as st
import altair as alt
import pandas as pd 
import numpy as np

# # 001-單純顯示文字 
# st.write('Hello World!')

# # 002-顯示按紐+if功能
# st.header('st.button')
# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')

# # 003-標題、滑桿小工具、顯示平方計算結果
# st.title('嗨你好，這是我的第一個streamlit')
# x = st.slider('選擇一個數值')
# st.write(f'{x}的平方是{x**2}')

# # 004-理解(rerun)機制>>>只要有跟小工具互動就會重新執行(eg.如拖動滑桿、點擊按鈕或在輸入框中輸入文字。)
# count = 0
# increment = st.button('增加')
# if increment:
#     count += 1
# st.write(f'計數 = {count}')

# 005-常用功能介紹
# st.title('title')
# st.header('header')
# st.subheader('subheader')
# st.write('Hello, *World!* :sunglasses:')
# st.write(1234)
# df = pd.DataFrame({
#      '*World!*': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

# sql = """
# select 
# Player_ID,
# Player_CreateTime
# from 
# uba.t11_player"""
# st.code(sql)

# latex = """
# y = ax^2+b
# """
# st.latex(latex)

# # 006-markdown功能>將 Markdown 語法 和 HTML 語法轉換成網頁上實際的樣式。
# st.markdown("這不是標題")
# st.markdown("# 這是一級標題 (H1)")
# st.markdown("## 這是二級標題 (H2)")
# st.markdown("### 這是三級標題 (H3)")
# st.markdown("#### 這是四級標題 (H4)")
# st.markdown("這段文字包含 **粗體** 和 *斜體*。")
# st.markdown("您也可以混合使用，像這樣 ***又粗又斜***。")
# st.markdown("這是上方的內容。")
# st.markdown("---") # 分隔線只需要三個減號
# st.markdown("這是下方的內容。")
# st.markdown("> 這是一段引言，通常會用來凸顯某個重點或名言佳句。")
# st.markdown("歡迎訪問 [Streamlit 官方文件](https://docs.streamlit.io/)。")

# # 007-st.dataframe、st.table
# df = pd.DataFrame({
#     'player_id': ['163008','163010','176583'],
#     'level': [37,53,8]
# })
# st.dataframe(df)
# st.write("---")
# st.write(df)
# st.markdown("---")
# st.table(df) ## table 是使用者不可以手動調整的格式
# st.markdown("---")

# 008-st.metric  ### 可以顯示升降的KPI指標! 
# kpi_today = 65
# kpi_yesterday = 66
# delta = kpi_today - kpi_yesterday
# st.metric('change of revenue',kpi_today,delta)

# 009-核取方塊
# st.checkbox("請勾我",True)
# count = 0
# if st.checkbox("請勾我A"):
#     count +=1
# if st.checkbox("請勾我B"):
#     count +=1
# if st.checkbox("請勾我C"):
#     count +=1
# st.metric('select me',count,count)

# 010-單選按鈕(radio)、下拉式選單(selectbox)
choice = st.selectbox('please select one you like',('A','B','C'))
choice = st.radio('please select one you like',('A','B','C'))
st.markdown(f"choice: *{choice}*")
st.header("楓之谷Artale調查")
st.markdown("---")
st.subheader("問題一：您的角色職業是？")
q1_choice = st.radio(
     label="請選擇目前的轉職職稱",
     options=["十字軍", "騎士", "龍騎士", "冰雷魔導士", "火毒魔導士", "祭司", "遊俠", "弩弓手", "神偷", "暗殺者", "格鬥家", "神槍手"],
     captions=["劍士", "劍士", "劍士", "法師", "法師", "法師", "弓箭手", "弓箭手", "盜賊", "盜賊", "海盜", "盜賊"],
     horizontal=True,
)
st.info(f'您的職業是: **{q1_choice}**')

# 底下的rerun按紐
st.button('rerun')
