Sure — here’s the updated README without the deployment link 👇 (copy-paste ready)

🫁 Pneumonia Detection using Chest X-ray

This project detects Pneumonia vs Normal from chest X-ray images using a CNN model trained with TensorFlow/Keras and deployed using Streamlit.

📌 Dataset

Kaggle - Chest X-ray (Pneumonia)
🔗 https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/data

🛠 Tech Stack

Python

TensorFlow

Keras

Streamlit

📂 Data Split

The original training dataset contains 5216 images.

It is split into:

Training Set: 4798 images

Validation Set: 418 images

The Kaggle test dataset is used for final evaluation.

🧹 Data Preprocessing & Augmentation
✅ Applied on Training Set:

Width shift

Height shift

Brightness shift

Rotation

Zoom

Pixel intensity variation (channel_shift)

Fill mode

Pixel normalization using rescale

✅ Applied on Validation & Test Set:

Pixel normalization using rescale

🖼 Input Configuration

Image size: 64 × 64

Batch size: 32

Model Training

A custom CNN model is trained for binary classification (Pneumonia / Normal).

Loss Function: Binary Crossentropy

Optimizer: Adam

Output Layer: Sigmoid

📊 Results (Test Set)
Metric	Score
Accuracy	92.95%
Recall	98.46%
Precision	91%
▶️ How to Run Locally
1) Clone the repository
git clone <your-repo-link>
cd <your-repo-folder>

2) Install dependencies
pip install -r requirements.txt

3) Run the Streamlit app
streamlit run app.py

📌 Notes

This project focuses on building an end-to-end pipeline:

Dataset preprocessing

CNN training + evaluation

Streamlit interface for prediction
