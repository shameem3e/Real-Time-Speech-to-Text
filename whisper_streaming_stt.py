import os
import queue
import tempfile
import sounddevice as sd
import numpy as np
from datetime import datetime
from faster_whisper import WhisperModel
import config

q = queue.Queue()
TRANSCRIPT_DIR = "transcripts"
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
TRANSCRIPT_FILE = os.path.join(TRANSCRIPT_DIR, "transcript.txt")

def save_transcript(text):
    if not text.strip():
        return
    with open(TRANSCRIPT_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {text}\n")

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(indata.copy())

def run_whisper():
    print("[INFO] Loading Faster-Whisper model...")
    model = WhisperModel(config.WHISPER_MODEL_SIZE, device="cuda" if os.environ.get("CUDA_VISIBLE_DEVICES") else "cpu", compute_type="float16")

    print("[INFO] Starting microphone stream (Whisper)... Press Ctrl+C to stop.")
    sample_rate = 16000
    block_size = 5  # seconds per chunk
    audio_buffer = []

    with sd.InputStream(samplerate=sample_rate, channels=1, dtype="float32", callback=callback):
        while True:
            data = q.get()
            audio_buffer.extend(data[:, 0])

            if len(audio_buffer) >= sample_rate * block_size:
                audio_chunk = np.array(audio_buffer, dtype=np.float32)
                audio_buffer = []

                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
                    import soundfile as sf
                    sf.write(tmpfile.name, audio_chunk, sample_rate)

                    segments, _ = model.transcribe(tmpfile.name)
                    for segment in segments:
                        print(f"\nYou said: {segment.text}")
                        save_transcript(segment.text)
