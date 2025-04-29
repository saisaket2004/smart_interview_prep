# 🤖 Smart Interview Analyzer AI

An AI-powered mock interview platform to help students polish their communication, emotional intelligence, and speaking fluency before facing real-world interviews.

---

## 🧠 Why This Project?

Many students struggle with confidence, clarity, and tone during interviews. **Smart Interview Analyzer AI** acts like a virtual mentor — analyzing your **speech**, **emotion**, and **grammar** to deliver instant, targeted feedback that helps you improve with every response.

---

## 🔍 What It Does

This tool provides:
- 🎤 **Voice Analysis** – Measures pitch & pace to gauge energy and clarity  
- 😐 **Facial Emotion Tracking** – Reads expressions to detect confidence, confusion, or nervousness  
- ✍️ **Speech Transcript Enhancement** – Gives you raw, cleaned-up, and grammatically improved transcripts  
- 📥 **Flexible Answer Input** – Supports live recordings or `.wav` file uploads  
- ⚡ **Instant Feedback** – Get real-time suggestions after each answer

---

## 🛠️ Technology Stack

### 📌 Frontend
- Built with `Streamlit` for an interactive and lightweight web UI.

### 📌 Backend (Python-based)
- `SpeechRecognition` – Converts voice to text  
- `Librosa` – Extracts audio features like pitch and tempo  
- `gTTS` – Reads out feedback using Google’s Text-to-Speech  
- `OpenCV` – Captures video frames for face detection  
- `NLTK` / `LanguageTool` – Enhances and corrects grammar in transcripts  
- `DeepFace` *(optional)* – Interprets facial emotions using deep learning models

---

## 🎯 How to Use It

1. Choose your **interview type** (Technical, HR, or Managerial).
2. Pick your **experience level** (Entry, Mid, or Senior).
3. Record your answer live or upload a `.wav` file.
4. The AI engine processes your input and returns:
   - Emotion metrics
   - Voice tone stats (pitch & tempo)
   - A multi-version transcript (raw, cleaned, and corrected)
5. Improve based on the AI feedback and try again!

---

## 📊 Upcoming Features

- Overall interview performance scores  
- Session tracking with improvement history  
- Personalized best-practice suggestions  
- Interactive dashboard for long-term progress  

---

## 🙏 Built With Help From

Thanks to the open-source ecosystem that powered this tool:

- `DeepFace`  
- `gTTS`  
- `Librosa`  
- `OpenCV`  
- `SpeechRecognition`  
- `NLTK` / `LanguageTool`  
