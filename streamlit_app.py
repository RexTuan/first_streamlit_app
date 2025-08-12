##[memo]
# streamlit檔案只要存檔, 會實時同步至網頁中!

import streamlit as st

# 001-單純顯示文字 
st.write('Hello World!')

# 002-顯示按紐+if功能
st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# 003-標題、滑桿小工具、顯示平方計算結果
st.title('嗨你好，這是我的第一個streamlit')
x = st.slider('選擇一個數值')
st.write(f'{x}的平方是{x**2}')

## 004-理解(rerun)機制>>>只要有跟小工具互動就會重新執行(eg.如拖動滑桿、點擊按鈕或在輸入框中輸入文字。)
count = 0
increment = st.button('增加')
if increment:
    count += 1
st.write(f'計數 = {count}')