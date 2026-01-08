import streamlit as st

st.set_page_config(page_title="My Streamlit App with GA4")

# Inject GA script into <head>
GA_HEAD_INJECT = """
<script>
(function(){
    const GA_ID = "G-MSRPEJMXBR";

    // Inject GA Script
    const script = document.createElement("script");
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
    document.head.appendChild(script);

    // Init dataLayer + gtag
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;

    gtag('js', new Date());
    gtag('config', GA_ID, { send_page_view: true });

})();
</script>
"""

# Inject to page with unsafe
st.markdown(GA_HEAD_INJECT, unsafe_allow_html=True)

# ====== Main App Content ======
st.title("Streamlit + GA4 Tracking")
st.title("^_^")
st.write("這是一個已經插入 Google Analytics (GA4) 的 Streamlit App 🎉")

# Optional: Trigger SPA page_view
st.markdown("""
<script>
if (window.gtag) {
    gtag('event', 'page_view', {
        page_title: document.title,
        page_path: window.location.pathname
    });
}
</script>
""", unsafe_allow_html=True)
