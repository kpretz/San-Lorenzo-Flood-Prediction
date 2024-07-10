import streamlit as st

st.header('San Lorenzo River Streamflow Prediction, Santa Cruz, California')


st.write('The results here are a personal project, primarily for education purposes and are not intended for use as a flood warning.')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')


precip = st.number_input('next precip')