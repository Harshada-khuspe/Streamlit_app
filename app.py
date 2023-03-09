import streamlit as st

st.title(":red[Data scince] internship-Data app")
st.header("Hi, I'm :red[Harshada Narayan Khuspe ]") 
st.subheader("A Developer")
st.subheader("From Satara")
st.write("click here for [linkedin](https://www.linkedin.com/in/harshada-khuspe-06394a225)")
st.write("click here for [github](https://github.com/Harshada-khuspe)")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()