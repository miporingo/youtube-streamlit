import streamlit as st
import numpy as np
import pandas as pd
import time


st.title('Streamlit 超入門')
st.write('DataFrame')

df =pd.DataFrame({
    '１列目':[1,2,3,4],
    '２列目':[10,20,30,40]
})
st.dataframe(df)

st.table (df.style.highlight_max(axis=0))

df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.area_chart(df)

st.bar_chart(df)

df = pd.DataFrame(
     np.random.rand(100,2)/[50,50] + [35.69,139.70],
     columns=['lat','lon']
)
st.map(df)

option = st.selectbox(
    'あたなが好きな数字を教えて下さい',
    list(range(1,11))
)

'あなたが好きな数字は数字は',option,'です。'

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
                   
#text =st.sidebar.text_input('あなたの趣味を教えて下さい')
#condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

#'あなたの趣味：',text
#'コンデション',condition

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせを書く')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせを書く')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせを書く')
expander = st.beta_expander('問い合わせ4')
expander.write('問い合わせを書く')
expander = st.beta_expander('問い合わせ5')
expander.write('問い合わせを書く')


