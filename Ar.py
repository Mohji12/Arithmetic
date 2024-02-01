import streamlit as st 

st.header('Welcome to my First APP of Streamlit :sunglasses:',divider='rainbow')
s1 = '1.Please Select First Value'
s1 = f"<p style='font-size:35px; font-family:Gill Sans Extrabold, sans-serif;'>{s1}</p>"
st.markdown(s1,unsafe_allow_html=True)
A = st.slider('v1',0,100)
v1 = "The Fisrt Value is"
v1 = f"<p style='font-size:25px; font-family:Gill Sans Extrabold, sans-serif;'>{v1}</p>"
st.markdown(v1,unsafe_allow_html=True)
a1 = f"<p style='font-size:25px; color:lightgreen ; font-family:Gill Sans Extrabold, sans-serif;'>{A}</p>"
st.markdown(a1,unsafe_allow_html=True)
# Second Value
s2 = '2.Please Select Second Value'
s2 = f"<p style='font-size:35px;font-family:Gill Sans Extrabold, sans-serif;'>{s2}</p>"
st.markdown(s2,unsafe_allow_html=True)
B = st.slider('v2',0,100)
v2 = "The Second Value is"
v2 = f"<p style='font-size:25px; font-family:Gill Sans Extrabold, sans-serif;'>{v2}</p>"
st.markdown(v2,unsafe_allow_html=True)
a1 = f"<p style='font-size:25px; color:lightgreen ;font-family:Gill Sans Extrabold, sans-serif;'>{B}</p>"
st.markdown(a1,unsafe_allow_html=True)

# "Arithmetic Operation"

# ADD
st.header('Two Numbers Arithmetic Operations :sunglasses:',divider='rainbow')

add = 'The Addition of Two Number is:'
s1 = f"<p style='font-size:40px; color:Orange ;font-family:Gill Sans Extrabold, sans-serif;'>{add}</p>"
st.markdown(s1,unsafe_allow_html=True)
Sum = A + B
s = f"<p style='font-size:30px; color:purple; font-family:Gill Sans Extrabold, sans-serif;'>{Sum}</p>"
st.markdown(s,unsafe_allow_html=True)

# Sub
minus = 'The Substraction of Two Number is:'
s2 = f"<p style='font-size:40px; color:Orange ;font-family:Gill Sans Extrabold, sans-serif;'>{minus}</p>"
st.markdown(s2,unsafe_allow_html=True)
Sub = A - B
s = f"<p style='font-size:30px; color:purple; font-family:Gill Sans Extrabold, sans-serif;'>{Sub}</p>"
st.markdown(s,unsafe_allow_html=True)

# Multiplication
prod = 'The product of Two Number is:'
s3 = f"<p style='font-size:40px; color:Orange ;font-family:Gill Sans Extrabold, sans-serif;'>{prod}</p>"
st.markdown(s3,unsafe_allow_html=True)
Multi = A * B
s = f"<p style='font-size:30px; color:purple; font-family:Gill Sans Extrabold, sans-serif;'>{Multi}</p>"
st.markdown(s,unsafe_allow_html=True)

# division
div = 'The Division of Two Number is:'
s4 = f"<p style='font-size:40px; color:Orange ;font-family:Gill Sans Extrabold, sans-serif;'>{div}</p>"
st.markdown(s4,unsafe_allow_html=True)
division1 = A / B
s = f"<p style='font-size:30px; color:purple; font-family:Gill Sans Extrabold, sans-serif;'>{division1}</p>"
st.markdown(s,unsafe_allow_html=True)

#Power
p = 'The power A**B of Two Number is:'
s5 = f"<p style='font-size:40px; color:Orange ;font-family:Gill Sans Extrabold, sans-serif;'>{p}</p>"
st.markdown(s5,unsafe_allow_html=True)
power = A**B
s = f"<p style='font-size:30px; color:purple; font-family:Gill Sans Extrabold, sans-serif;'>{power}</p>"
st.markdown(s,unsafe_allow_html=True)




