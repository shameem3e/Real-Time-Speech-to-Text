import sounddevice as sd
import queue
import json
import os
from datetime import datetime
from vosk import Model, KaldiRecognizer
import config

q = queue.Queue()
TRANSCRIPT_DIR = "transcripts"
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
TRANSCRIPT_FILE = os.path.join(TRANSCRIPT_DIR, "transcript.txt")

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

def save_transcript(text):
    if not text.strip():
        return
    with open(TRANSCRIPT_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {text}\n")

def run_vosk():
    if not os.path.exists(config.VOSK_MODEL_PATH):
        raise FileNotFoundError(f"VOSK model not found at {config.VOSK_MODEL_PATH}")

    print("[INFO] Loading VOSK model...")
    model = Model(config.VOSK_MODEL_PATH)
    recognizer = KaldiRecognizer(model, 16000)

    print("[INFO] Starting microphone stream (VOSK)... Press Ctrl+C to stop.")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                if result.get("text"):
                    print("\nYou said:", result["text"])
                    save_transcript(result["text"])
            else:
                partial = json.loads(recognizer.PartialResult())
                if partial.get("partial"):
                    print(f"\rPartial: {partial['partial']}", end="")
