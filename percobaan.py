import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Player Soccer')
st.header('ini adalah tujuk utama')
st.subheader ('tajuk 1')
st.caption('ini caption')

# kode
code_python =""""
def fungsi (parameter):
    print ('ini adalah kode python')
"""

st.code(code_python, language='python')

st.text('ini text')

# st.latex //latex generator

df = pd.DataFrame({
    'nim': ['2209116016','2209116005'],
    'nama': ['imelda', 'alisya']
})
st.dataframe(data=df, width=1000, height=50)
st.table(data=df)

st.metric(label='Suhu', value='100 F', delta='1.2 F')

x = np.random.normal(15,5,250)
fig,ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

# x = np.random.normal(15,5,250)
# fig,ax = plt.subplots()
# sns.histplot(x=x)
# st.pyplot(fig)