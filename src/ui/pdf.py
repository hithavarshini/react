import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
def pdf_display(path):
    page_to_show = st.session_state.get('pdf_page', None)
    if page_to_show:
        return pdf_viewer(
            path,
            height=800,
            width=700,
            pages_to_render=[page_to_show]
        )
    else:
        return pdf_viewer(
            path,
            height=800,
            width=700
        )