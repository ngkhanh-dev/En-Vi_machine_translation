import streamlit as st
from transformers import pipeline

# Tạo pipeline dịch thuật
translator = pipeline(model="ngdangkhanh/en-vi-mbart50", device=0)  # `device=0` để chạy trên GPU


# Giao diện Streamlit
st.title("English to Vietnamese Translator")

# Nhập văn bản tiếng Anh
english_text = st.text_area("Enter English text:", height=150)

# Xử lý dịch thuật
if english_text:
    # beam search
    #print(english_text)
    translated_text = translator(english_text, batch_size=32, num_beams=5)[0]['generated_text']
    #print(translated_text)
    st.text_area("Vietnamese Translation:", translated_text, height=150)

