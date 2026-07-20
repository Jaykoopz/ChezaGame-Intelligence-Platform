import streamlit as st


def show_header():
    st.markdown("""
    <style>
    .cip-header{
        background: linear-gradient(90deg,#1565C0,#1E88E5);
        padding:25px;
        border-radius:15px;
        margin-bottom:20px;
        color:white;
    }

    .cip-title{
        font-size:38px;
        font-weight:700;
        margin-bottom:5px;
    }

    .cip-subtitle{
        font-size:18px;
        opacity:0.9;
    }

    .cip-version{
        margin-top:10px;
        font-size:14px;
        opacity:0.8;
    }
    </style>

    <div class="cip-header">

        <div class="cip-title">
            ⚽ ChezaGame Intelligence Platform
        </div>

        <div class="cip-subtitle">
            Powered by ChezaAI
        </div>

        <div class="cip-version">
            Version 2.0 • Foundation
        </div>

    </div>
    """, unsafe_allow_html=True)