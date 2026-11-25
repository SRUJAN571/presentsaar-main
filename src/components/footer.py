import streamlit as st

def footer_home():

    st.markdown(f"""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:30px">
        <p style="font-weight:bold;color:white;">Created with ❤️ by SRUJAN KS</p>
        
        </div>
    """, unsafe_allow_html=True)

def footer_dash():

    st.markdown(f"""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:30px">
        <p style="font-weight:bold;color:black;">Created with ❤️ by SRUJAN KS</p>
        
        </div>
    """, unsafe_allow_html=True)    