# 🧠 Virtual Human Interface – BTU Buddy

A real‑time, voice‑driven **Virtual Human** system built for interactive human‑computer communication. The system captures spoken input, transcribes it with Whisper, generates context‑aware responses using OpenAI GPT, converts them to lifelike speech with Coqui TTS, and sends facial blendshape data to Unreal Engine for animated avatar rendering.

---

## 🚀 Tech Stack

| Layer             | Technology                   | Purpose                              |
| ----------------- | ---------------------------- | ------------------------------------ |
| **Input & Audio** | `sounddevice`, `simpleaudio` | Microphone capture & playback        |
| **ASR**           | **OpenAI Whisper**           | Speech‑to‑text transcription         |
| **LLM**           | **OpenAI GPT‑3.5‑Turbo**     | Natural‑language response generation |
| **TTS**           | **Coqui TTS**                | Neural text‑to‑speech synthesis      |
| **Animation**     | ARKit‑style blendshapes      | Facial expression parameters         |
| **Game Engine**   | **Unreal Engine 5**          | Avatar animation & rendering         |
| **Communication** | HTTP `POST` (`requests`)     | Python → Unreal data transfer        |
| **Environment**   | Python 3.10 (Conda)          | Runtime platform                     |

---

## 🧩 Project Structure

```
Virtual_Human/
├── main.py                 # Orchestrates all modules
├── asr.py                  # Whisper‑based transcription
├── nlp.py                  # OpenAI GPT integration
├── tts.py                  # Coqui TTS synthesis & playback
├── lip.py                  # Generates ARKit blendshapes
├── captured_audio.wav      # Temporary audio storage
├── requirements.txt        # All Python deps
└── README.md               # Project documentation
```

---

## 🛠️ Setup Instructions

### 1 — Clone the repository

```bash
git clone https://github.com/iamtarunshyam/Virtual_Human.git
cd Virtual_Human
```

### 2 — Create & activate Conda environment *(Python 3.10)*

```bash
conda create -n virtualhuman python=3.10 -y
conda activate virtualhuman
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

> **Note :** `TTS` and `whisper` currently require Python ≤3.10.

### 4 — Set your OpenAI API Key

```bash
export OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
```

*or* create a `.env` file:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
```

---

## ▶️ Running the Application

```bash
python main.py
```

The system will:

1. Welcome you via TTS.
2. Listen for your spoken question.
3. Generate a GPT response.
4. Speak the answer aloud.
5. Send blendshape data to Unreal for avatar animation.

---

## 🔄 Unreal Engine Integration

`lip.py` posts ARKit blendshape JSON to:

```
http://localhost:8080/apply_blendshapes
```

Make sure Unreal Engine (or Omniverse → Unreal bridge) is running an HTTP listener on that endpoint—either via **Remote Control API**, a Python script, or plugins such as **VaRest** / **Web Remote Control**.

---

## 📦 Dependencies (excerpt)

```
openai==0.28.1
TTS
whisper
simpleaudio
sounddevice
requests
python-dotenv
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🌐 .env Template

Create `.env` or copy from `.env.example`:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 📸 Demo

> *(Add screenshots or demo video/GIF here)*

---

## 📄 License

MIT License — free for academic and research use.

---

## 🙋‍♂️ Author

**Tarun Shyam**  |  MSc AI, BTU Cottbus  |  [@iamtarunshyam](https://github.com/iamtarunshyam)

