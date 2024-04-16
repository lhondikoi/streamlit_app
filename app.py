import streamlit as st
from utils import largest_of_three

st.title('Largest of Three')
st.caption('Find the largest of three numbers.')
st.divider()

col1, col2 = st.columns(2, gap='large')

with col1:
    number1 = st.number_input('Insert the first number', key='1', step=1)
    number2 = st.number_input('Insert the second number', key='2',step=1)
    number3 = st.number_input('Insert the third number', key='3', step=1)

with col2:
    st.write('The largest number is:')
    st.title(f'{largest_of_three(number1, number2, number3)}')