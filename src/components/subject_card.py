import streamlit as st
from html import escape
def subject_card(name,code,section,stats=None,footer_callback=None):
    stats_html = ""
    if stats:
        items = "".join(
            '<div style="background:#EB459E10; padding:5px 12px; border-radius:12px; font-size:0.9rem">'
            f'{icon} <b>{escape(str(value))}</b> {escape(str(label))}</div>'
            for icon, label, value in stats
        )
        stats_html = f'<div style="display:flex; gap:8px; flex-wrap:wrap;">{items}</div>'

    html = (
        '<div style="background:white; border:1px solid black; border-left:8px solid #EB459E; '
        'padding:25px; border-radius:20px; margin-bottom:20px">'
        f'<h3 style="margin:0; color:#1e293b; font-size:1.5rem">{escape(str(name))}</h3>'
        '<p style="color:#64748b; margin:10px 0">Code: '
        "<span style='background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px'>"
        f'{escape(str(code))}</span>'
        f' | Section: {escape(str(section))}</p>'
        f'{stats_html}'
        '</div>'
    )


    st.markdown(html,unsafe_allow_html=True)

    if footer_callback:
       footer_callback()