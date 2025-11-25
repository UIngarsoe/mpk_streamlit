mpk_main.py
# ----------------------------
# Main Streamlit MPK Engine
# ----------------------------
import streamlit as st
from mpk_config import load_config
from mpk_memory import load_memory
from mpk_utils import run_tools

from mpk_memory import save_upload, load_memory
from mpk_rss import fetch_rss_headlines
from mpk_utils import validate_vip, summarize_memory

st.set_page_config(
    page_title="🐉 MPK Engine: Myanmar War Crimes & NUG Insight",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# VIP Login
# ----------------------------
st.sidebar.title("🔒 VIP Login")
username = st.sidebar.text_input("Username")
code = st.sidebar.text_input("Access Code", type="password")

if not validate_vip(username, code):
    st.warning("❌ Invalid VIP credentials. Access denied.")
    st.stop()

# ----------------------------
# Upload Section
# ----------------------------
st.sidebar.header("📤 Upload New Memory / Knowledge")
with st.sidebar.form("upload_form"):
    upload_title = st.text_input("Title of upload")
    upload_type = st.selectbox("Type", ["Table", "Code", "Note", "PDF"])
    upload_content = st.text_area("Content", height=150)
    submitted = st.form_submit_button("Save Upload")
    if submitted and upload_content:
        save_upload(username, upload_title, upload_content, upload_type)
        st.success("✅ Upload saved to MPK memory!")

# ----------------------------
# Chat / Query Section
# ----------------------------
st.title("🐉 MPK Engine: Myanmar NUG / PDF Insights")
st.subheader("Ask about PDF, PDT, PRF, or NUG operations")

query = st.text_input("Enter your question")
if query:
    memory_entries = load_memory(username)
    summary = summarize_memory(memory_entries)

    st.markdown("### 🧠 MPK 3-P Summary")
    for key in ["People", "Power", "Practice"]:
        st.markdown(f"**{key}:**")
        for item in summary[key]:
            st.markdown(f"- {item}")

    st.markdown("### 📌 Current Updates from News")
    rss_updates = fetch_rss_headlines()
    for u in rss_updates[:5]:
        st.markdown(f"- {u['source']}: [{u['title']}]({u['link']})")

