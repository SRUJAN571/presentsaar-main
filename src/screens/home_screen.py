import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.footer import footer_home
def home_screen():
    

    header_home()
    style_background_home()
    style_base_layout()






    col1,col2=st.columns(2,gap='large')

    with col1:
        st.header("I'm Teacher")
        st.image("https://static.vecteezy.com/system/resources/previews/034/990/520/non_2x/teacher-esport-mascot-logo-design-vector.jpg",width=120)
        if(st.button("Teacher Portal",type='primary',icon=':material/arrow_outward:',icon_position='right')):
            st.session_state['login_type']='teacher'
            st.rerun()

    with col2:
        st.header("I'm Student")
        st.image("https://cdn.vectorstock.com/i/1000v/40/93/boy-student-mascot-logo-design-vector-32124093.jpg",width=120)
        if(st.button("Student Portal",type='primary',icon=':material/arrow_outward:',icon_position='right')):
            st.session_state['login_type']='student' 
            st.rerun()
    footer_home()