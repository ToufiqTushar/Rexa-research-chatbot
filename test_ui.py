import streamlit as st

st.set_page_config(page_title="HTML Test")

st.markdown(
    """
    <style>
        .test-box {
            background: black;
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            font-size: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.html(
    """
    <div class="test-box">
        HTML IS WORKING
    </div>
    """
)