import streamlit as st


def show_intelligence_center(ai):
    st.markdown("---")

    st.subheader("🧠 ChezaAI Intelligence Center")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Decision Score",
            f"{ai['score']}/100"
        )

    with c2:
        st.metric(
            "Risk Level",
            ai['risk']
        )

    with c3:
        st.metric(
            "Confidence",
            ai['confidence']
        )

    st.markdown("### 💡 Today's Insight")
    st.info(ai['insight'])

    st.markdown("### 🎯 Recommended Action")
    st.success(ai['recommendation'])