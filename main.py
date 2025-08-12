import config
from vosk_streaming_stt import run_vosk
from whisper_streaming_stt import run_whisper

if __name__ == "__main__":
    print("🎤 Real-Time Speech-to-Text with Transcript Saving")
    print("[INFO] Mode:", config.MODE.upper())
    print("[INFO] Transcript will be saved to transcripts/transcript.txt\n")

    if config.MODE == "vosk":
        run_vosk()
    elif config.MODE == "whisper":
        run_whisper()
    else:
        raise ValueError("Invalid MODE in config.py. Use 'vosk' or 'whisper'.")
