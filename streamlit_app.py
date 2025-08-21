##[memo]
"""
streamlit檔案只要存檔, 會實時同步至網頁中!
"""
import streamlit as st
import altair as alt
import pandas as pd 
import numpy as np
import plotly.express as px
import random
from streamlit_extras.card import card 

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

# # 013-text_input單行文字輸入框
# text = st.text_input("欲回覆訊息請在此輸入。")
# st.success(F"您輸入的訊息:{text}")

# # 014-date_input日期選擇棄
# var_date = st.date_input("欲回覆訊息請在此輸入。")
# st.success(F"您輸入的訊息:{var_date}")

# # 015-sidebar側邊欄
# st.sidebar.title("側邊欄範例")
# st.sidebar.write("這是側邊欄的內容。")
# st.sidebar.header("選項")
# option = st.sidebar.selectbox(
#     "選擇一個選項",
#     ("選項1", "選項2", "選項3")
# )
# st.sidebar.write(f"您選擇的選項是: {option}")
# # 在主頁面顯示選擇的選項
# st.write(f"您在側邊欄選擇的選項是: {option}") 
# # 這裡可以添加更多的側邊欄內容，例如輸入框、按鈕等

# # 016-(gemini示範區)
# st.sidebar.header("實時輸入")
# user_input = st.sidebar.text_input("請輸入一些文字:")
# if user_input:
#     st.sidebar.write(f"您輸入的文字是: {user_input}")

#     # --- 側邊欄 (Sidebar) ---
# st.sidebar.header("⚙️ 控制面板")

# # 使用 st.sidebar.selectbox 讓使用者選擇圖表類型
# chart_type = st.sidebar.selectbox(
#     "1. 請選擇圖表類型：",
#     ("長條圖", "折線圖")
# )

# # 使用 st.sidebar.slider 讓使用者選擇要生成的數據點數量
# num_points = st.sidebar.slider(
#     "2. 請選擇數據點數量：",
#     min_value=5,
#     max_value=50,
#     value=20,
#     step=1
# )

# st.sidebar.write("---") # 在側邊欄中也可以用分隔線

# # 使用 st.sidebar.button 作為一個觸發器
# if st.sidebar.button("產生隨機數據！"):
#     st.sidebar.success("數據已更新！")


# # --- 主畫面 (Main Page) ---
# st.title("📊 動態圖表產生器")
# st.write(f"您正在檢視：**{chart_type}**，包含 **{num_points}** 個數據點。")

# # 根據側邊欄的選擇來生成數據
# # np.random.randn 會生成符合常態分佈的隨機數
# data = pd.DataFrame({
#     'x': np.arange(num_points),
#     'y': np.random.randn(num_points),
#     'category': np.random.choice(['A', 'B', 'C'], num_points)
# })

# # 根據側邊欄的選擇來繪製不同的圖表
# if chart_type == "長條圖":
#     fig = px.bar(data, x='x', y='y', color='category', title="隨機長條圖")
# else: # 折線圖
#     fig = px.line(data, x='x', y='y', color='category', title="隨機折線圖")

# # 在主畫面顯示圖表
# st.plotly_chart(fig, use_container_width=True)

# st.write("---")
# st.write("原始數據：")
# st.dataframe(data)

# # 017-tabs分頁
# st.set_page_config(layout="wide") # 讓頁面寬一點，更像儀表板

# st.title("📊 銷售數據分析報告")

# # --- 準備範例數據 ---
# @st.cache_data # 快取數據，避免每次互動都重新生成
# def create_data():
#     data = {
#         '日期': pd.to_datetime(pd.date_range(start='2025-07-01', periods=31, freq='D')),
#         '銷售額': np.random.randint(5000, 15000, size=31),
#         '顧客數': np.random.randint(50, 150, size=31),
#         '產品類別': np.random.choice(['電子產品', '服飾', '家居用品'], size=31)
#     }
#     return pd.DataFrame(data)

# df = create_data()

# # --- 使用 st.tabs 創建分頁 ---
# tab_viz, tab_data, tab_summary = st.tabs(["📈 資料視覺化", "📄 原始數據", "📝 數據摘要"])

# with tab_viz:
#     st.header("選擇產品類別")
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         product_category = st.selectbox("請選擇產品類別", df['產品類別'].unique())
#         filtered_df = df[df['產品類別'] == product_category]
#     st.header("銷售趨勢圖")
#     # 創建一個下拉選單，讓使用者選擇要看的指標
#     metric_to_plot = st.selectbox("請選擇指標", ("銷售額", "顧客數"))
    
#     # 繪製折線圖
#     fig = px.line(df, x='日期', y=metric_to_plot, title=f'{metric_to_plot} 時間趨勢')
#     st.plotly_chart(fig, use_container_width=True)

# with tab_data:
#     st.header("完整原始數據")
#     # 顯示可互動的 DataFrame
#     st.dataframe(df, use_container_width=True)

# with tab_summary:
#     st.header("數據基本統計摘要")
#     # 顯示 Pandas 的 describe() 結果
#     st.table(df.describe())

# if st.sidebar.button("產生隨機數據！"):
#     st.sidebar.success("數據已更新！")

#use st.container(), st.sidebar(), st.columns()

# # 018-container 排版用功能(將所有功能併入同一區)
# st.header("使用 with 語句")

# with st.container(border=True):
#     st.write("這個區塊裡的所有東西都在同一個 container 中。")
#     st.info("這是一個提示訊息。")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.image("https://static.streamlit.io/examples/dog.jpg")
#     with col2:
#         st.write("您甚至可以在 container 內部再使用 st.columns 進行排版！")

# st.write("這段文字在 container 的外面。")

# image_url = f"https://maplestory.io/api/GMS/210.1.1/mob/100004/render/stand" #菇菇寶貝

# st.title("從 MapleStory.io 抓取道具圖片")
# st.image(image_url, width=50)

# # 019-st.session_state 實現狀態保持 + 衝捲模擬器
st.set_page_config(page_title="機率模擬器", page_icon="🎲")

SCROLL_DATA = {
    "10%卷軸": "https://maplestory.io/api/THMS/20.1.0/item/2046328/icon?resize=4", 
    "60%卷軸": "https://maplestory.io/api/THMS/20.1.0/item/2046318/icon?resize=4", 
    "30%詛咒卷軸": "https://maplestory.io/api/THMS/20.1.0/item/2046771/icon?resize=4", 
    "70%詛咒卷軸": "https://maplestory.io/api/THMS/20.1.0/item/2046332/icon?resize=4", 
    }

if 'use_count' not in st.session_state:
    st.session_state.use_count = 0  #已使用次數
    st.session_state.pass_count = 0 #衝成功次數
    st.session_state.total_chances = 7 #初始可衝次數
    st.session_state.last_result = None # 用來記錄上一次的結果 (成功/失敗/無)
    st.session_state.cant_use = 0 # 用來記錄是否無法使用卷軸

# --- 動態計算 ---
if st.session_state.last_result != -1:
    remaining_chances = st.session_state.total_chances - st.session_state.use_count
else:
    remaining_chances = 0

# --- 介面顯示 ---
st.markdown("## 機率模擬器 ![m](https://maplestory.io/api/GMS/210.1.1/mob/100004/render/stand)")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    button_name = "10%卷軸"
    image_url = SCROLL_DATA[button_name]
    button_label = f"{button_name}  ![{button_name}]({image_url}) "
    if st.button(button_label, key=f'{button_name}', use_container_width=True):
        if remaining_chances <= 0:
            st.session_state.cant_use = 1
        else:
            st.session_state.use_count += 1
            if random.random() < 0.1:
                st.session_state.pass_count += 1
                st.session_state.last_result = 1
            else:
                st.session_state.last_result = 0
            st.rerun()
with col2:
    button_name = "60%卷軸"
    image_url = SCROLL_DATA[button_name]
    button_label = f"{button_name}  ![{button_name}]({image_url}) "
    if st.button(button_label, key=f'{button_name}', use_container_width=True):
        if remaining_chances <= 0:
            st.session_state.cant_use = 1
        else:
            st.session_state.use_count += 1
            if random.random() < 0.6:
                st.session_state.pass_count += 1
                st.session_state.last_result = 1
            else:
                st.session_state.last_result = 0
            st.rerun()
with col3:
    button_name = "30%詛咒卷軸"
    image_url = SCROLL_DATA[button_name]
    button_label = f"{button_name}  ![{button_name}]({image_url}) "
    if st.button(button_label, key=f'{button_name}', use_container_width=True):
        if remaining_chances <= 0:
            st.session_state.cant_use = 1
        else:
            st.session_state.use_count += 1
            if random.random() < 0.3:
                st.session_state.pass_count += 1
                st.session_state.last_result = 1
            elif random.random() > 0.65: #摧毀道具

                st.session_state.last_result = -1
            else:
                st.session_state.last_result = 0
            st.rerun()
with col4:
    button_name = "70%詛咒卷軸"
    image_url = SCROLL_DATA[button_name]
    button_label = f"{button_name}  ![{button_name}]({image_url}) "
    if st.button(button_label, key=f'{button_name}', use_container_width=True):
        if remaining_chances <= 0:
            st.session_state.cant_use = 1
        else:
            st.session_state.use_count += 1
            if random.random() < 0.7:
                st.session_state.pass_count += 1
                st.session_state.last_result = 1
            elif random.random() > 0.85: #摧毀道具

                st.session_state.last_result = -1
            else:
                st.session_state.last_result = 0
            st.rerun()

st.write("---")
st.write(f"目前可衝數量：{remaining_chances}")
st.write(f"目前成功數量：{st.session_state.pass_count}")

if st.session_state.cant_use == 1:
    st.error("此裝備不具可衝次數，請換件試試！")
else: 
    if st.session_state.last_result == None:
        st.success("   ")
    elif st.session_state.last_result == 1:
        st.success("卷軸閃爍了一下，神秘的力量傳到了道具身上。")
    elif st.session_state.last_result == 0:
        st.error("卷軸閃爍了一下，但道具沒有任何變化。")
    elif st.session_state.last_result == -1:
        st.error("卷軸閃爍了一下，道具被摧毀了。")

if st.button("![~s](https://maplestory.io/api/THMS/20.1.0/mob/100006/render/move)換件裝備"):
    # 遍歷 session_state 中的所有 key 並將它們刪除
    keys_to_delete = list(st.session_state.keys())
    for key in keys_to_delete:
        del st.session_state[key]
    # 重新整理頁面，強制觸發初始化
    st.rerun()

# 020-
