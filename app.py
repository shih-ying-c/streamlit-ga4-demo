import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="My Streamlit App with GA4")

# ===== GA4 / gtag.js Tracking Script =====
GA_SCRIPT = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MSRPEJMXBR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-MSRPEJMXBR');
</script>
"""

# Inject script to page
components.html(GA_SCRIPT, height=0, width=0)

# ==== Main App Content ====
st.title("Streamlit + GA4 Tracking")
st.write("這是一個已經插入 Google Analytics (GA4) 的 Streamlit App 🎉")

