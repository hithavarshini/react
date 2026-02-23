import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
def pdf_display(path,num):
    return pdf_viewer(
        path,
        height=500,
        width=500,
        pages_to_render=[num]
    )