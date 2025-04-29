# 🎓 Smart Interview Analyzer AI for Student Interview Prep

Helping students prepare smarter for interviews through **AI-driven feedback** on speech, emotion, and grammar.

---

## 📚 Project Overview

**Smart Interview Analyzer AI** is an advanced mock interview system designed to help students improve their:

- Communication skills  
- Emotional intelligence  
- Verbal fluency  

It acts as a **personal virtual interview coach**, analyzing:

- Voice tone  
- Facial emotions  
- Speech transcripts  

And provides **real-time, actionable feedback** to build confidence and identify improvement areas before real interviews.

---

## ✨ Key Features

### 🎙 Voice Tone Analysis
- Extracts **pitch (Hz)** and **tempo (BPM)**
- Detects signs of **monotony**, **enthusiasm**, or **nervousness**

### 🎭 Facial Emotion Detection
- Identifies **dominant facial expressions** such as:
  - Confidence
  - Confusion
  - Nervousness

### 📝 Speech Transcript Correction
- Provides:
  - **Raw transcript**
  - **Improved transcript (clarified)**
  - **Grammar-corrected, professional transcript**

### 🔄 Flexible Input
- Record live answers using webcam/microphone
- Or upload pre-recorded `.wav` files

### 📈 Real-Time Feedback
- Instant suggestions after each answer:
  - Improve fluency
  - Enhance expressiveness
  - Correct grammar issues

---

## ⚙️ How It Works

1. **Choose Interview Domain**: Technical / HR / Managerial  
2. **Select Experience Level**: Entry / Mid / Senior  
3. **Input Answer**: Record live or upload a `.wav` file  
4. **Receive Instant Analysis**:
   - 🎭 Dominant Emotion Detection (via video)
   - 🎙 Voice Pitch & Tempo Analysis
   - 📝 Transcripts with Grammar Corrections
5. **Get Actionable AI-Powered Feedback** to improve future responses

---

## 🛠 Tech Stack

### Frontend
- `Streamlit` — Python-based interactive web app framework

### Backend
- `Python`

### Libraries Used
- `OpenCV` — For facial detection & emotion recognition
- `SpeechRecognition` — Converts audio to text
- `Google Text-to-Speech (gTTS)` — Provides audio feedback
- `NLTK` / `LanguageTool` — Grammar correction
- `Librosa` — Audio feature extraction (pitch, tempo)
- `DeepFace` *(optional)* — Facial emotion analysis

---

## 🚀 Future Enhancements

- Add an **Overall Interview Scoring System**
- **Track performance** across multiple interview attempts
- Provide **Best Practice Suggestions** after each answer
- Build a **Dashboard** for tracking progress over time

---

## 🙌 Acknowledgements

Thanks to the open-source tools and models that enabled fast prototyping:

- DeepFace  
- Librosa  
- gTTS  
- SpeechRecognition  
- OpenCV  
- NLTK / LanguageTool  

---

## 💻 Demo (Optional)

*Add your deployment link or demo video here.*
