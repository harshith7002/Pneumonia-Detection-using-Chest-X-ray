import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("classification-model.keras")
model = load_model()
class_names = ["Normal", "Pneumonia"]
st.set_page_config(page_title="Pneumonia Detector", layout="centered")
st.title("🩺 Chest X-ray Pneumonia Detector")
st.write("Upload a chest X-ray (64x64 input expected) to classify as **Normal** or **Pneumonia**.")
uploaded_file = st.file_uploader("Upload Chest X-ray", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded X-ray", use_column_width=True)
    img_resized = img.resize((64, 64))
    x = np.array(img_resized) / 255.0
    x = np.expand_dims(x, axis=0)
    prob = model.predict(x)[0][0]
    pred = 1 if prob >= 0.5 else 0
    confidence = prob if pred == 1 else 1 - prob
    st.subheader("Prediction")
    st.write(f"**Class:** {class_names[pred]}")
    st.write(f"**Confidence:** {confidence:.2f}")
