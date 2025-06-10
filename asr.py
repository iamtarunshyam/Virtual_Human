# asr/asr_engine.py

import whisper
import os
import logging

class ASR:
    def __init__(self, model_name="base", device="cpu"):
        """
        Initialize the ASR engine with a specified Whisper model.

        Args:
            model_name (str): Whisper model size (e.g., 'tiny', 'base', 'small', 'medium', 'large').
            device (str): Device to run the model on ('cpu' or 'cuda').
        """
        logging.info(f"Loading Whisper model: {model_name} on {device}")
        self.model = whisper.load_model(model_name, device=device)
        self.device = device

    def transcribe(self, audio_file: str) -> str:
        """
        Transcribe the given audio file to text.

        Args:
            audio_file (str): Path to the audio file.

        Returns:
            str: Transcribed text.
        """
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file {audio_file} not found.")
        
        logging.info(f"Transcribing audio file: {audio_file}")
        result = self.model.transcribe(audio_file)
        return result['text']

    def capture_audio(self, duration=5, sample_rate=16000, output_file="captured_audio.wav"):
        """
        Capture audio using the microphone.

        Args:
            duration (int): Duration of the audio capture in seconds.
            sample_rate (int): Sampling rate for the audio.
            output_file (str): File path to save the captured audio.

        Returns:
            str: Path to the saved audio file.
        """
        import sounddevice as sd
        import numpy as np
        import scipy.io.wavfile as wav

        logging.info(f"Capturing audio for {duration} seconds...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait for the recording to finish

        # Save the recorded audio to a WAV file
        wav.write(output_file, sample_rate, audio_data)
        logging.info(f"Audio captured and saved to {output_file}")

        return output_file

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example usage
    asr = ASR(model_name="base", device="cpu")

    # Capture audio from microphone
    audio_path = asr.capture_audio(duration=5)

    # Transcribe audio file
    transcription = asr.transcribe(audio_path)
    print("Transcription:", transcription)
