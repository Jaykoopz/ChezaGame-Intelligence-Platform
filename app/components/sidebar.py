import streamlit as st


def show_sidebar():
    with st.sidebar:

        st.image(
            "https://img.icons8.com/fluency/96/football2.png",
            width=80
        )

        st.title("ChezaGame")

        st.caption("Sports Decision Intelligence")

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Analytics",
                "Reports",
                "ChezaAI",
                "Settings"
            ]
        )

        st.divider()

        uploaded_file = st.file_uploader(
            "Upload CBAS_Database.xlsx",
            type=["xlsx"]
        )

        st.divider()

        st.header("Filters")

        return page, uploaded_file