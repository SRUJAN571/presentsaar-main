import streamlit as st
def header_home():
    logo_url = "https://img.magnific.com/premium-vector/student-with-book-logo-vector-education-logo-template-design-concept-student-progress-suc_980985-2249.jpg?semt=ais_hybrid&w=740&q=80"
    st.markdown(f"""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:30px">
            <img src="{logo_url}" style="height:100px;" />
            <h1 style="text-align:center;color: #E0E3FF">Present<br> Saar</h1>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://img.magnific.com/premium-vector/student-with-book-logo-vector-education-logo-template-design-concept-student-progress-suc_980985-2249.jpg?semt=ais_hybrid&w=740&q=80"
    st.markdown(f"""
        <div style="display:flex;flex-direction:flex;align-items:center;justify-content:center; gap:10px;">
            <img src="{logo_url}" style="height:85px;" />
            <h2 style="text-align:center;color: #5865F2">Present<br> Saar</h2>
        </div>
    """, unsafe_allow_html=True)
