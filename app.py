import streamlit as st
from model import predict

st.set_page_config(
    page_title="Sarcasm Detection using BERT",
    page_icon="😏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.title("😏 Sarcasm Detector")

    st.markdown("---")

    st.subheader("About")

    st.write("""
This application predicts whether a news headline is **Sarcastic** or **Not Sarcastic** using a fine-tuned **BERT (bert-base-uncased)** model.

**Model**
- BERT Base
- PyTorch
- Transformers
- Streamlit
""")

    st.markdown("---")

    st.subheader("How to Use")

    st.write("""
1. Enter a news headline.
2. Click **Predict**.
3. View prediction and confidence.
""")

    st.markdown("---")

    st.subheader("Sample Headlines")

    st.caption("Try these examples:")

    st.code("Area Man Passionate Defender Of What He Imagines Constitution To Be")

    st.code("Government Announces New Education Policy")

    st.code("Scientists Discover Water On Mars")

    st.markdown("---")

    st.caption("Made with BERT")

# ---------------- Main Page ---------------- #

st.title("📰 Sarcasm Detection using BERT")

st.markdown("""
Detect whether a **news headline** is sarcastic using a **Deep Learning model built on BERT Transformer Architecture**.
""")

st.divider()

headline = st.text_area(
    "Enter News Headline",
    placeholder="Example: Local man claims eating pizza daily is key to longevity...",
    height=150
)

col1, col2 = st.columns([1, 5])

with col1:
    predict_button = st.button("Predict", use_container_width=True)

if predict_button:

    if headline.strip() == "":
        st.warning("⚠ Please enter a news headline.")

    else:

        with st.spinner("Analyzing headline..."):

            prediction, probability = predict(headline)

        confidence = probability * 100

# ---------------- Confidence Level ---------------- #

        if confidence >= 90:
            level = "🟢 Very High"
            color = "success"

        elif confidence >= 75:
            level = "🟢 High"
            color = "success"

        elif confidence >= 60:
            level = "🟡 Moderate"
            color = "warning"

        else:
            level = "🟠 Low"
            color = "warning"

        st.divider()

        st.subheader("Prediction")

        if prediction == "Sarcastic":
            st.error("😏 **Sarcastic Headline**")
        else:
            st.success("📰 **Not Sarcastic**")

        st.subheader("Confidence Level")

        if color == "success":
            st.success(level)
        else:
            st.warning(level)

        with st.expander("📊 Technical Details"):

            st.metric(
                label="Model Confidence",
                value=f"{confidence:.2f}%"
    )

            st.progress(confidence / 100)

            if confidence < 60:
                st.info(
            "The model is less confident about this prediction. "
            "Sarcasm often depends on subtle context and wording."
        )

        st.divider()

        st.subheader("Input Headline")

        st.info(headline)

# ---------------- Footer ---------------- #

st.divider()

st.caption(
    "Built with Streamlit • PyTorch • Hugging Face Transformers • BERT"
)