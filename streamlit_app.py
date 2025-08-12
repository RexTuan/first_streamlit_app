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
st.title('title')
st.header('header')
st.subheader('subheader')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)
df = pd.DataFrame({
     '*World!*': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

sql = """
select 
Player_ID,
Player_CreateTime
from 
uba.t11_player"""
st.code(sql)

latex = """
y = ax^2+b
"""
st.latex(latex)

st.button('rerun')
