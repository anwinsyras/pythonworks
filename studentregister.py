
import streamlit as st
n=st.text_input("Name")
a=st.number_input("Age")
d=st.date_input("DOB")
e=st.text_input("Email")
g=st.radio("gender",['male','female'])
c=st.selectbox("courses",['python','dotnet','testing','java'])
b=st.button('register')
if b:
    st.write("name:",n)
    st.write("age:",a)
    st.write("DateOfBirth:",d)
    st.write("email:",e)
    st.write("gender:",g)
    st.write("course:",c)