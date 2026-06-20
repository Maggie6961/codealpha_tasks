import streamlit as st
import random
from music21 import stream, note, instrument

st.title("🎵 AI Music Generator")

st.write("Generate a simple AI melody.")

genre = st.selectbox(
    "Select Style",
    ["Classical", "Jazz", "Pop"]
)

if st.button("Generate Music"):

    melody = stream.Stream()

    if genre == "Classical":
        melody.append(instrument.Piano())
    elif genre == "Jazz":
        melody.append(instrument.Saxophone())
    else:
        melody.append(instrument.ElectricPiano())

    scale = ['C4','D4','E4','F4','G4','A4','B4','C5']

    for i in range(20):
        pitch = random.choice(scale)
        n = note.Note(pitch)
        n.quarterLength = random.choice([0.5, 1])
        melody.append(n)

    melody.write('midi', fp='generated_music.mid')

    st.success("Music Generated Successfully!")

    with open("generated_music.mid", "rb") as file:
        st.download_button(
            label="Download Music",
            data=file,
            file_name="generated_music.mid"
        )
