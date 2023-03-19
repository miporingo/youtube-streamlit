import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamit 超入門')
st.write('Hello, World!')
st.write('DateFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.write(df)

st.dataframe(df)

import streamlit as st
from streamlit_sortables import sort_items

st.subheader('リストのソート')
original_items = list('FGABCDE')
sorted_items  = sort_items(original_items)
 
st.write('---')
st.write(f'並び変え前: {original_items}')
st.write(f'並び変え後: {sorted_items}')
st.write('---')


