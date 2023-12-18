import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

st.write("""
# My first app
Hello *world!*
Hynnah Baker 
""")

st.header("test html import")

HtmlFile = open("calculator_UI.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code)
 
