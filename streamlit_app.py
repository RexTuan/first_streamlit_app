import streamlit as st

# 001-單純顯示文字 
st.write('Hello World!')

# 002-顯示按紐+if功能
st.header('st.button')

if st.header('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
