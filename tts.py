# tts/tts_engine.py

import logging
from TTS.api import TTS
import os

class TTSGenerator:
    def __init__(self, 
                 model_name="tts_models/en/vctk/vits", 
                 speaker="p280", 
                 output_dir="tts_output"):
        """
        Initialize the TTS generator.

        Args:
            model_name (str): The name of the TTS model to use.
            speaker (str): The speaker ID for voice selection (if supported by the model).
            output_dir (str): Directory to save generated audio files.
        """
        logging.info("Initializing Coqui TTS engine")
        self.tts = TTS(model_name)
        self.speaker = speaker
        self.output_dir = output_dir

        # Create the output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def synthesize(self, text: str, output_file: str = "response.wav") -> str:
        """
        Synthesize speech from text and save it as an audio file.

        Args:
            text (str): The text to be synthesized.
            output_file (str): Name of the output audio file.

        Returns:
            str: Path to the generated audio file.
        """
        try:
            logging.info(f"Synthesizing speech for text: {text}")
            output_path = os.path.join(self.output_dir, output_file)

            # Generate speech with the specified speaker and save the output
            self.tts.tts_to_file(text=text, speaker=self.speaker, file_path=output_path)
            logging.info(f"Audio saved to {output_path}")

            return output_path
        except Exception as e:
            logging.error(f"Error during speech synthesis: {e}")
            return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example usage
    tts_gen = TTSGenerator()
    sample_text = "Hello! I am your virtual assistant. How can I help you today?"
    audio_path = tts_gen.synthesize(sample_text)

    if audio_path:
        print(f"Audio file generated: {audio_path}")
    else:
        print("Failed to generate audio.")
