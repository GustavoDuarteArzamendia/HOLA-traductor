
import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
import tempfile
import os

st.set_page_config(page_title="HOLA Traductor", page_icon="🌐")

st.title("🌍 Traductor Inteligente HOLA (versión web)")
st.markdown("Traducí texto en segundos y escuchalo en otro idioma.")

texto = st.text_area("✍️ Escribí algo para traducir:", height=150)

idioma_destino = st.selectbox(
    "🌐 Elegí el idioma al que querés traducir:",
    ["en", "fr", "pt", "it", "de", "ru", "zh-CN"],
    format_func=lambda x: {
        "en": "Inglés",
        "fr": "Francés",
        "pt": "Portugués",
        "it": "Italiano",
        "de": "Alemán",
        "ru": "Ruso",
        "zh-CN": "Chino simplificado"
    }.get(x, x)
)

if st.button("🎯 Traducir"):
    if texto.strip() == "":
        st.warning("Por favor escribí algo para traducir.")
    else:
        try:
            traduccion = GoogleTranslator(source='auto', target=idioma_destino).translate(texto)
            st.success("✅ Traducción:")
            st.markdown(f"**{traduccion}**")

            # Generar audio
            tts = gTTS(text=traduccion, lang=idioma_destino)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts.save(tmp_file.name)
                st.audio(tmp_file.name, format="audio/mp3")
                os.unlink(tmp_file.name)
        except Exception as e:
            st.error(f"❌ Error al traducir o generar audio: {e}")
