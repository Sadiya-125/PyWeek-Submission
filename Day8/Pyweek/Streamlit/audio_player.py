import streamlit as st
import base64

def play_audio_from_base64(audio_base64: str, key: str = "audio"):
    """Display audio player for base64 encoded audio"""
    if audio_base64:
        try:
            audio_html = f"""
            <audio controls style="width: 100%;">
                <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
                Your browser does not support audio playback.
            </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Could not play audio: {str(e)}")
    else:
        st.info("No audio available")
