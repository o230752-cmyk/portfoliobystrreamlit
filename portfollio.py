import streamlit as st
st.set_page_config(
    page_title="akhil",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <hr style="border: none; height: 2px; background-color: white;">
    """,
    unsafe_allow_html=True,
)
tab1,tab2,tab3=st.tabs(["Home","Projects","Skills"])
with tab1:


 col1,col2=st.columns(2)
with col1:
    st.markdown("---")
    st.header("GEN AI ENGENEER")
    st.markdown("**AKHIL KURAPATI at RGUKT**")
    st.markdown("**student at RGUKT (2nd year)**")
    co1,co2=st.columns(2)
    with co1:
       st.link_button("Contact me","tel:+917671070015")
    with co2:
      st.link_button("linkdin","https://www.linkedin.com/in/akhil-kurapati-0b8b3b3b3/")
    st.markdown("---")
with col2:
    st.image("/portfolio/WhatsApp Image 2026-06-16 at 1.25.23 PM.jpeg",width=300)


st.markdown(
    """
    <hr style="border: none; height: 2px; background-color: white;">
    """,
    unsafe_allow_html=True,
)
with tab2:
    st.markdown("# Projects")
    st.markdown("**1st year projects**")
    st.write("1.Basic level chatbot using python modules and  other python concepts")
    st.write("2.portfolio website using streamlit")
    st.write("3.student database mangament using python libraries")
with tab3:
    st.markdown("# Skills")
    st.write("python programming")
    st.image("/portfolio/python.jpeg",width=500)
    st.write("Introduction to ai")
    st.image("/portfolio/simp.jpeg",width=500)
    st.write("prompt engneering")
    st.image("/portfolio/prompt.jpeg",width=500)
