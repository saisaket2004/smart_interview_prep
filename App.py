import streamlit as st
import tempfile
import os
import cv2
import av
import whisper
import google.generativeai as genai
from deepface import DeepFace
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import numpy as np
import moviepy.editor as mp

# ----------------------------
# CONFIGURATION
# ----------------------------
st.set_page_config(page_title="AI Speech+Emotion Insight", layout="centered")
st.title("🎥 AI-Powered Communication Insight")

# 🔐 Gemini API key (use your actual key here)
GEMINI_API_KEY = "Type_your_API_Key"
genai.configure(api_key=GEMINI_API_KEY)

# ----------------------------
# VIDEO CAPTURE SETUP
# ----------------------------
class VideoRecorder(VideoTransformerBase):
    def __init__(self):
        self.frame = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        self.frame = img
        return img

ctx = webrtc_streamer(key="video", video_transformer_factory=VideoRecorder, desired_playing_state=True)
record_frames = []

def save_video(frames, filename):
    if not frames:
        return None
    height, width, _ = frames[0].shape
    out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 10, (width, height))
    for f in frames:
        out.write(f)
    out.release()
    return filename

# ----------------------------
# ANALYSIS & FEEDBACK
# ----------------------------
if ctx.video_transformer:
    st.info("📽️ Your webcam is live. Click below to stop and analyze.")
    if st.button("Stop Recording & Analyze"):
        st.success("Processing video...")

        while ctx.video_transformer.frame is not None:
            record_frames.append(ctx.video_transformer.frame)
            ctx.video_transformer.frame = None

        video_path = os.path.join(tempfile.gettempdir(), "user_recording.mp4")
        save_video(record_frames, video_path)

        # 1. Facial Emotion Detection
        try:
            result = DeepFace.analyze(video_path, actions=["emotion"], enforce_detection=False)
            facial_emotion = result[0]["dominant_emotion"]
        except:
            facial_emotion = "Unable to detect"

        # 2. Audio Transcription & Sentiment
        clip = mp.VideoFileClip(video_path)
        audio_path = video_path.replace(".mp4", ".wav")
        clip.audio.write_audiofile(audio_path, logger=None)

        whisper_model = whisper.load_model("base")
        whisper_result = whisper_model.transcribe(audio_path)
        transcript = whisper_result['text']

        sentiment_analyzer = SentimentIntensityAnalyzer()
        sentiment_score = sentiment_analyzer.polarity_scores(transcript)
        speech_sentiment = "positive" if sentiment_score["compound"] > 0.05 else "negative" if sentiment_score["compound"] < -0.05 else "neutral"

        # 3. Gemini Feedback
        with st.spinner("🤖 Generating feedback with Gemini..."):
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            prompt = f"""
            You are a communication expert. Analyze the user's speaking behavior using the following:

            - Detected facial emotion: {facial_emotion}
            - Detected speech sentiment: {speech_sentiment}
            - Full transcription: "{transcript}"

            Provide a short, constructive, and human-like feedback combining emotional expression and verbal tone. Include soft-skill improvement tips if needed.
            """
            gemini_response = model.generate_content(prompt)
            insight = gemini_response.text.strip()

        # 4. Final Output
        st.video(video_path)
        st.subheader("🧠 AI Insight Report")
        st.markdown(f"- **Facial Emotion**: `{facial_emotion}`")
        st.markdown(f"- **Speech Sentiment**: `{speech_sentiment}`")
        st.markdown(f"- **Transcription**: {transcript}")
        st.success(insight)
