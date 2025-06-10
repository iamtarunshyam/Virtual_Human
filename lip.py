import os
import json
import subprocess
import logging
from tts import TTSGenerator  # Assumes tts.py is already implemented and working

def locate_wav2lip():
    """Locate the Wav2Lip directory or prompt the user for its location."""
    wav2lip_path = os.path.abspath("Wav2Lip")
    if not os.path.exists(wav2lip_path):
        logging.error(f"Wav2Lip directory not found at {wav2lip_path}")
        user_input_path = input("Please provide the absolute path to the Wav2Lip directory: ").strip()
        if os.path.exists(user_input_path):
            wav2lip_path = user_input_path
        else:
            raise FileNotFoundError(f"Wav2Lip directory still not found at {user_input_path}")
    return wav2lip_path

def generate_lip_sync(audio_path):
    """Run Wav2Lip to generate a lip-synced video and extract blendshapes."""
    try:
        # Step 1: Locate Wav2Lip directory
        wav2lip_path = "/Users/tarunshyam/Wav2Lip"

        # Step 2: Run Wav2Lip
        logging.info("Running Wav2Lip for lip sync...")
        output_video_path = os.path.join("output/video", "lip_synced_video.mp4")
        subprocess.run([
            "python", "inference.py",
            "--checkpoint_path", "checkpoints/wav2lip_gan.pth",
            "--face", "/Users/tarunshyam/Virtual Human/Prod/Tarun Linkedin.jpeg",
            "--audio", audio_path,
            "--outfile", output_video_path
        ], check=True, cwd=wav2lip_path)

        # Step 3: Extract blendshapes (Placeholder logic)
        logging.info("Extracting blendshapes from video...")
        blendshapes = {
            "jawOpen": 0.8,
            "mouthSmileLeft": 0.5,
            "mouthSmileRight": 0.5
        }
        blendshapes_output_path = os.path.join("output/blendshapes", "blendshapes.json")
        with open(blendshapes_output_path, "w") as f:
            json.dump(blendshapes, f)

        return blendshapes_output_path

    except FileNotFoundError as e:
        logging.error(f"File or directory not found: {e}")
        return None
    except subprocess.CalledProcessError as e:
        logging.error(f"Wav2Lip failed: {e}")
        return None

def send_blendshapes_to_unreal(blendshapes_path):
    """Send ARKit blendshapes to Unreal Engine via HTTP."""
    try:
        with open(blendshapes_path, "r") as f:
            blendshapes = json.load(f)

        unreal_endpoint = "http://localhost:8080/apply_blendshapes"
        response = requests.post(unreal_endpoint, json=blendshapes)

        if response.status_code == 200:
            logging.info("Blendshapes sent successfully to Unreal Engine.")
        else:
            logging.error(f"Failed to send blendshapes: {response.status_code}")

    except Exception as e:
        logging.error(f"Error sending blendshapes to Unreal: {e}")

def main():
    logging.basicConfig(level=logging.INFO)

    # File path provided by user
    audio_path = "/Users/tarunshyam/Virtual Human/Prod/tts_output/welcome.wav"

    # Generate lip sync and extract blendshapes
    blendshapes_path = generate_lip_sync(audio_path)
    if not blendshapes_path:
        logging.error("Failed to generate blendshapes.")
        return

    # Send blendshapes to Unreal Engine
    send_blendshapes_to_unreal(blendshapes_path)

if __name__ == "__main__":
    main()
