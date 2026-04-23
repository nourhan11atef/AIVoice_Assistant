# 🎙️ Virtual Voice Assistant

A Python-based virtual voice assistant that listens to your voice commands and responds intelligently. It can play YouTube videos, tell you the current date and time, and fetch Wikipedia summaries — all hands-free!

---

## 🚀 Features

- 🎵 **Play YouTube Videos** — Say *"play [song/video name]"* and it opens YouTube automatically
- 📅 **Get Today's Date** — Say *"date"* to hear today's date
- ⏰ **Get Current Time** — Say *"time"* to hear the current time
- 📖 **Wikipedia Search** — Say *"tell me about [topic]"* to get a quick summary
- 🔊 **Text-to-Speech** — Responds back to you using a natural voice

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `speech_recognition` | Captures and converts voice to text |
| `pyttsx3` | Converts text to speech (offline) |
| `pywhatkit` | Plays YouTube videos |
| `wikipedia` | Fetches topic summaries |
| `datetime` | Provides date and time info |

---

## 📦 Installation


### 1. Install Dependencies

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyaudio
```

> ⚠️ **Note for Windows users:** If `pyaudio` fails to install, download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually.

> ⚠️ **Note for Linux users:** Run `sudo apt-get install portaudio19-dev python3-pyaudio` before pip install.

---

## ▶️ Usage

```bash
python virtual_voice_assistant.py
```

Once running, the assistant will say **"I am listening... you can ask"** — then speak your command clearly into the microphone.

### 🗣️ Example Commands

| What You Say | What It Does |
|---|---|
| *"play shape of you"* | Opens and plays the video on YouTube |
| *"what is the date"* | Speaks today's date |
| *"what is the time"* | Speaks the current time |
| *"tell me about Python"* | Reads a Wikipedia summary of Python |

---

## 📁 Project Structure

```
virtual-voice-assistant/
│
├── virtual_voice_assistant.py   # Main assistant script
└── README.md                    # Project documentation
```

---

## 🔧 Troubleshooting

- **Microphone not detected:** Make sure your microphone is connected and set as default input device.
- **`UnknownValueError`:** The assistant couldn't understand your speech — try speaking more clearly in a quiet environment.
- **No voice output:** Check that your speakers/headphones are working and `pyttsx3` is installed correctly.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by nourhan using Python
