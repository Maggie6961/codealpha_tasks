import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip
import os

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
)

st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages.")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

source = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Select Target Language",
    list(languages.keys()),
    index=1
)

text = st.text_area(
    "Enter Text",
    height=150
)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed!")

        st.subheader("Translated Text")

        st.write(translated)

        if st.button("Copy to Clipboard"):
            pyperclip.copy(translated)
            st.success("Copied Successfully!")

        tts = gTTS(
            translated,
            lang=languages[target]
        )

        tts.save("voice.mp3")

        audio_file = open("voice.mp3", "rb")
        st.audio(audio_file.read())
