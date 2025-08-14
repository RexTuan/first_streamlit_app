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
# choice = st.selectbox('please select one you like',('A','B','C'))
# choice = st.radio('please select one you like',('A','B','C'))
# st.markdown(f"choice: *{choice}*")
# st.header("楓之谷Artale調查")
# st.markdown("---")
# st.subheader("問題一：您的角色職業是？")
# q1_choice = st.radio(
#      label="請選擇目前的轉職職稱",
#      options=["十字軍", "騎士", "龍騎士", "冰雷魔導士", "火毒魔導士", "祭司", "遊俠", "弩弓手", "神偷", "暗殺者", "格鬥家", "神槍手"],
#      captions=["劍士", "劍士", "劍士", "法師", "法師", "法師", "弓箭手", "弓箭手", "盜賊", "盜賊", "海盜", "盜賊"],
#      horizontal=True,
# )
# st.info(f'您的職業是: **{q1_choice}**')

# 011-多選下拉式選單(multiselect)
# selected_equipments = st.multiselect('請勾選裝備(多選)',['披風','鞋子'])
# st.markdown("---")
# # 012-輸入數值(number_input)
# if '披風' in selected_equipments:
#      st.markdown('##### 請輸入欲購買披風素質')
#      col1, col2, col3 = st.columns(3)
#      with col1:
#          var_cloak_str = st.number_input('請輸入力量(STR)',min_value=0,step=1,format="%d",key="var_cloak_str")
#      with col2:
#          var_cloak_dex = st.number_input('請輸入敏捷(DEX)',min_value=0,step=1,format="%d",key="var_cloak_dex")
#      with col3:
#          var_cloak_price = st.number_input('請輸入價格(雪花)',min_value=0,step=1,format="%d",key="var_cloak_price")
#      st.markdown('##### 請輸入現有披風素質')
#      col4, col5 = st.columns(2)
#      with col4:
#          var_current_cloak_str = st.number_input('請輸入*現有*披風力量(STR)',min_value=0,step=1,format="%d",key="var_current_cloak_str")
#      with col5:
#          var_current_cloak_dex = st.number_input('請輸入*現有*披風敏捷(DEX)',min_value=0,step=1,format="%d",key="var_current_cloak_dex")
#      var_cloak_ap = var_cloak_str + var_cloak_dex
#      var_current_cloak_ap = var_current_cloak_str + var_current_cloak_dex
#      if st.button("確認",key='cloak'):
#         st.success(f"您欲購買**{var_cloak_ap}**屬(**{var_cloak_str}**力**{var_cloak_dex}**敏)披風，價格為**{var_cloak_price}**雪。")
#         st.success(f"目前裝備**{var_current_cloak_ap}**屬(**{var_current_cloak_str}**力**{var_current_cloak_dex}**敏)披風。")
#      st.markdown('---')
# if '鞋子' in selected_equipments:
#      st.markdown('##### 請輸入欲購買鞋子素質')
#      col1, col2, col3 = st.columns(3)
#      with col1:
#          var_shoes_str = st.number_input('請輸入力量(STR)',min_value=0,step=1,format="%d",key="var_shoes_str")
#      with col2:
#          var_shoes_dex = st.number_input('請輸入敏捷(DEX)',min_value=0,step=1,format="%d",key="var_shoes_dex")
#      with col3:
#          var_shoes_price = st.number_input('請輸入價格(雪花)',min_value=0,step=1,format="%d",key="var_shoes_price")
#      st.markdown('##### 請輸入現有鞋子素質')
#      col4, col5 = st.columns(2) 
#      with col4:
#          var_current_shoes_str = st.number_input('請輸入*現有*鞋子力量(STR)',min_value=0,step=1,format="%d",key="var_current_shoes_str")
#      with col5:
#          var_current_shoes_dex = st.number_input('請輸入*現有*鞋子敏捷(DEX)',min_value=0,step=1,format="%d",key="var_current_shoes_dex")
#      var_shoes_ap = var_shoes_str + var_shoes_dex
#      var_current_shoes_ap = var_current_shoes_str + var_current_shoes_dex
#      if st.button("確認",key='shoes'):
#          st.success(f"您欲購買**{var_shoes_ap}**屬**{var_shoes_str}**力**{var_shoes_dex}**敏鞋子，價格為**{var_shoes_price}**雪。")
#          st.success(f"目前裝備**{var_current_shoes_ap}**屬**{var_current_shoes_str}**力**{var_current_shoes_dex}**敏鞋子。")
# # 底下的rerun按紐
# st.markdown('---')
# st.button('rerun')

# 012-(gemini示範區)
# --- 頁面標題與說明 ---
# st.title("⚔️ 裝備效益分析小工具")
# st.markdown("比較不同裝備的素質提升與價格，找出最划算的購買順序！")

# # --- 讓使用者選擇要比較的裝備 ---
# options = ['披風', '鞋子', '頭盔']
# selected_equipments = st.multiselect(
#     '請勾選您想比較的裝備（可複選）',
#     options,
#     default=['披風', '鞋子'] # 預設勾選兩項，方便測試
# )

# st.markdown("---")

# # --- 為每個選擇的裝備創建輸入區塊 ---
# # 使用一個字典來暫存使用者輸入的數值，方便後續處理
# input_data = {}

# for equipment in options:
#     if equipment in selected_equipments:
#         with st.expander(f"【{equipment}】的數值輸入區", expanded=True):
#             st.subheader(f"新 {equipment}（欲購買）")
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 new_dex = st.number_input(f'敏捷(DEX)', min_value=0, step=1, key=f"{equipment}_new_dex")
#             with col2:
#                 new_str = st.number_input(f'力量(STR)', min_value=0, step=1, key=f"{equipment}_new_str")
#             with col3:
#                 price = st.number_input(f'價格(雪花)', min_value=0, step=1, key=f"{equipment}_price")

#             st.subheader(f"舊 {equipment}（目前身上）")
#             col4, col5 = st.columns(2)
#             with col4:
#                 current_dex = st.number_input(f'敏捷(DEX)', min_value=0, step=1, key=f"{equipment}_current_dex")
#             with col5:
#                 current_str = st.number_input(f'力量(STR)', min_value=0, step=1, key=f"{equipment}_current_str")
            
#             # 將輸入的數據儲存到字典中
#             input_data[equipment] = {
#                 "new_dex": new_dex, "new_str": new_str, "price": price,
#                 "current_dex": current_dex, "current_str": current_str
#             }

# st.markdown("---")

# # --- 計算與顯示結果 ---
# # --- 計算與顯示結果 ---
# if st.button("📊 開始計算最佳購買順序"):
    
#     results = []

#     # 遍歷使用者輸入的每一件裝備數據
#     for name, data in input_data.items():
#         # 計算總提升素質
#         stat_gain = (data["new_dex"] - data["current_dex"]) + (data["new_str"] - data["current_str"])
        
#         # 計算每點素質的成本
#         # 關鍵的 edge case 處理：如果素質沒有提升，成本視為無限大
#         if stat_gain <= 0:
#             cost_per_stat = float('inf') # 無限大，排序時會自動排到最後
#         else:
#             cost_per_stat = data["price"] / stat_gain
            
#         results.append({
#             "裝備名稱": name,
#             "總提升素質": stat_gain,
#             "價格": data["price"],
#             "每點素質成本": cost_per_stat # <-- 正確的 key 名稱為中文
#         })

#     # 處理沒有任何有效裝備可計算的情況
#     if not results:
#         st.warning("請至少選擇一件裝備並輸入數值才能進行計算。")
#     else:
#         # ▼▼▼ 修正點：將 key 從 "cost_per_stat" 改為正確的 "每點素質成本" ▼▼▼
#         sorted_results = sorted(results, key=lambda x: x["每點素質成本"])
        
#         st.subheader("📈 計算結果分析")

#         # 使用 Pandas DataFrame 讓表格更美觀
#         df = pd.DataFrame(sorted_results)
        
#         # 格式化 DataFrame 的顯示
#         st.dataframe(
#             df.style.format({
#                 "每點素質成本": "{:,.2f}", # 格式化為有兩位小數的數字
#                 "價格": "{:,}" # 加上千分位符號
#             }),
#             use_container_width=True
#         )

#         # 產生最終的購買建議
#         # 篩選掉沒有提升的裝備
#         valuable_items = [item for item in sorted_results if item["總提升素質"] > 0]
        
#         if not valuable_items:
#             st.error("所有比較的裝備均無素質提升，沒有建議的購買順序。")
#         else:
#             recommendation_order = " > ".join([item["裝備名稱"] for item in valuable_items])
#             st.success(f"🎉 **建議購買順序為： {recommendation_order}**")
#             st.balloons()