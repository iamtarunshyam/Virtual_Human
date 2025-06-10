# main.py

import logging
import simpleaudio as sa
from asr import ASR
from nlp import GPTResponse
from tts import TTSGenerator

def play_audio(file_path):
    """
    Play an audio file using simpleaudio.
    """
    try:
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        logging.error(f"Error playing audio: {e}")

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Initialize modules
    asr = ASR()
    gpt = GPTResponse()
    tts = TTSGenerator()

    # Step 1: Initial Prompt
    print("Hi, I am your BTU Buddy, how can I support you?")
    welcome_audio_path = tts.synthesize("Hi, I am your BTU Buddy, how can I support you?", output_file="welcome.wav")

    # Play the welcome audio
    print("[INFO] Playing welcome audio...")
    play_audio(welcome_audio_path)

    # Step 2: Capture user input via ASR
    print("[INFO] Listening for your question...")
    audio_path = asr.capture_audio(duration=5)  # Capture 5 seconds of audio
    user_query = asr.transcribe(audio_path)

    print(f"[INFO] You said: {user_query}")

    # Step 3: Process input using NLP
    response_text = gpt.generate_response(user_query)
    print(f"[INFO] BTU Buddy Response: {response_text}")

    # Step 4: Convert response to speech and play it
    response_audio_path = tts.synthesize(response_text, output_file="response.wav")

    print("[INFO] Playing BTU Buddy's response...")
    play_audio(response_audio_path)

if __name__ == "__main__":
    main()
