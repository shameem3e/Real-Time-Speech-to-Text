# 📚 Real Time Speech to Text

A **real-time speech-to-text** system with **dual transcription modes**:
- **VOSK** → Fully offline, low latency
- **Faster-Whisper** → High accuracy with GPU/CPU support

The system:
- Streams audio from your microphone
- Transcribes in real time
- Saves transcripts to a text file
- Supports easy switching between modes in `config.py`

---

## 📌 Features

- 🎤 **Dual Mode** — Choose between:
  - **Offline Mode (VOSK)** — No internet needed, works on CPU
  - **High Accuracy Mode (Faster-Whisper)** — Uses GPU if available
- 📁 **Transcript Saving** — Every recognized phrase is saved to `transcripts/transcript.txt`
- 🖥 **Real-time Display** — Shows partial and final transcriptions in the console
- ⚡ **Low Latency** — Processes audio in near real time
- 🔄 **Easy Switching** — Change modes with one line in `config.py`

---

## 📂 Folder Structure

realtime_speech_to_text/

│

├── main.py # Entry point to run the app

├── config.py # Settings: mode, model paths, parameters

├── vosk_streaming_stt.py # Offline low-latency transcription (VOSK)

├── whisper_streaming_stt.py # High-accuracy GPU/CPU transcription (Faster-Whisper)

└── transcripts/

└── transcript.txt # Output file for transcripts


---

## ⚙️ Setup Guide

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/shameem3e/Real-Time-Speech-to-Text.git
cd Real-Time-Speech-to-Text

```
### **2️⃣ Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

```
### **3️⃣ Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt

```
Note:

* If using Whisper mode, you also need `ffmpeg` installed:

	* Windows: Install from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add to PATH

	* macOS: `brew install ffmpeg`

	* Linux: `sudo apt install ffmpeg`

### **4️⃣ Download models**
* VOSK (Offline mode):

	* Download from [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)

	* Example: `vosk-model-small-en-us-0.15`

	* Extract the folder and set the path in `config.py` → `VOSK_MODEL_PATH`

* Faster-Whisper (High accuracy mode):

	* Model size is set in `config.py` → `WHISPER_MODEL_SIZE`

	* Options: `"tiny"`, `"base"`, `"small"`, `"medium"`, `"large-v2"`

### **5️⃣ Run the project**
```bash
python main.py

```
You should see: 
```bash
🎤 Real-Time Speech-to-Text with Transcript Saving
[INFO] Mode: VOSK
[INFO] Transcript will be saved to transcripts/transcript.txt

Partial: hello
You said: hello world

```

### **✅ Example Output (VOSK Mode)**

You speak:
```bash
Hello, this is a test.

```

Console:
```bash
Partial: hello
You said: hello this is a test

```

transcripts/transcript.txt:
```bash
[2025-08-12 14:32:01] hello this is a test

```

## 📜 Code Overview

This project is divided into separate files for clarity and modularity:

### 1. `main.py`
- **Purpose:** Entry point of the project. Reads settings from `config.py` and launches the selected transcription mode.
- **Libraries used:**
  - `config` → Load mode and settings.
  - `vosk_streaming_stt` / `whisper_streaming_stt` → Calls the chosen engine.
- **Why:** Keeps the startup logic clean and mode switching simple.

---

### 2. `config.py`
- **Purpose:** Stores all configurable settings (mode, model paths, parameters).
- **Libraries used:** None (pure Python variables).
- **Why:** Allows changing between VOSK and Whisper without editing core code.

---

### 3. `vosk_streaming_stt.py`
- **Purpose:** Handles **offline low-latency transcription** using VOSK.
- **Libraries used:**
  - `vosk` → Speech recognition model.
  - `sounddevice` → Captures audio from microphone in real time.
  - `json` → Parses recognition output from VOSK.
  - `datetime` → Timestamping transcripts.
- **Why:** VOSK provides a fast and offline recognition option, ideal for low-resource environments.

---

### 4. `whisper_streaming_stt.py`
- **Purpose:** Handles **high-accuracy streaming transcription** using Faster-Whisper.
- **Libraries used:**
  - `faster_whisper` → Loads and runs Whisper model with GPU/CPU.
  - `sounddevice` → Captures audio chunks from microphone.
  - `soundfile` → Temporarily saves chunks for processing.
  - `numpy` → Handles audio buffers efficiently.
  - `datetime` → Timestamping transcripts.
- **Why:** Faster-Whisper offers better accuracy for complex or accented speech, with GPU acceleration support.

---

### 5. `transcripts/transcript.txt`
- **Purpose:** Stores every recognized phrase with a timestamp.
- **Libraries used:** None (plain text file).
- **Why:** Keeps a permanent log for later review or analysis.

## ❓ FAQ
Q: Do I need the internet?

A: No, if you use VOSK mode. Yes, if you use Whisper mode with models not cached locally.

Q: Does it work on GPU?

A: Yes, Faster-Whisper can use CUDA for acceleration.

Q: Can I use another language?

A: Yes, download the respective VOSK/Whisper language model.

Q: Where are transcripts saved?

A: In `transcripts/transcript.txt`


## 🛠 Tech Stack
* Python 3.8+
* VOSK
* Faster-Whisper
* Sounddevice
* Soundfile
* Numpy
* FFmpeg (for Whisper mode)

## 🚀 Future Improvements
* 🌍 Add Google Search integration for answering questions
* 📝 Save transcripts in JSON format with timestamps
* 🎯 Add speaker diarization (identify different speakers)
* 📡 WebSocket API for real-time browser display
* 📱 Mobile-friendly version

## 👨‍💻 Author
[MD. Shameem Ahammed](https://sites.google.com/view/shameem3e)

Graduate Student | AI & ML Enthusiast

---

---
