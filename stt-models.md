# 🧠 Speech-to-Text (STT) Models

> **Comprehensive collection of open-source and production-ready STT models, libraries, and tools for offline and real-time transcription.**

---

## 📋 **Table of Contents**
- [🔥 Whisper-Based Models](#-whisper-based-models)
- [⚙️ Traditional & Real-Time STT Engines](#️-traditional--real-time-stt-engines)
- [🧠 PyTorch-Based Frameworks](#-pytorch-based-frameworks)
- [🧪 Lightweight & Embedded STT](#-lightweight--embedded-stt)
- [📚 Utility Libraries](#-utility-libraries)

---

## 🔥 **Whisper-Based Models**

### 🔷 [OpenAI Whisper](https://github.com/openai/whisper)
- **Type**: Multilingual and multitask ASR
- **Features**: Speech recognition, translation, language ID
- **Training**: 680,000 hours of web audio
- **Usage**: Easy-to-use CLI and Python API
- **Best for**: General-purpose transcription

### 🔷 [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- **Type**: Optimized Whisper implementation
- **Features**: Fast inference using CTranslate2
- **Deployment**: CPU/GPU/edge devices
- **Usage**: Drop-in replacement for Whisper
- **Best for**: Production deployments

### 🔷 [WhisperX](https://github.com/m-bain/whisperX)
- **Type**: Enhanced Whisper with timestamps
- **Features**: Word-level timestamps + speaker diarization
- **Integration**: PyAnnote for speaker separation
- **Best for**: Detailed transcription analysis

---

## ⚙️ **Traditional & Real-Time STT Engines**

### 🔷 [Kaldi](https://github.com/kaldi-asr/kaldi)
- **Type**: Academic speech recognition framework
- **Features**: Gold standard for research
- **Complexity**: Requires advanced setup
- **Best for**: Research and custom ASR pipelines

### 🔷 [Vosk API](https://github.com/alphacep/vosk-api)
- **Type**: Real-time STT engine
- **Languages**: 20+ languages supported
- **Platforms**: Android, Raspberry Pi, desktop
- **Features**: Offline operation, lightweight
- **Best for**: Embedded and mobile applications

### 🔷 [DeepSpeech (Mozilla)](https://github.com/mozilla/DeepSpeech)
- **Type**: End-to-end STT engine
- **Framework**: TensorFlow-based
- **Training**: English datasets (LibriSpeech, Common Voice)
- **Status**: Archived (Mozilla discontinued)
- **Best for**: Learning and legacy projects

---

## 🧠 **PyTorch-Based Frameworks**

### 🔷 [SpeechBrain](https://github.com/speechbrain/speechbrain)
- **Type**: All-in-one speech toolkit
- **Features**: ASR, speaker ID, enhancement, separation
- **Framework**: PyTorch-based
- **Documentation**: Well-documented
- **Best for**: Research and development

### 🔷 [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)
- **Type**: Real-time transcription pipeline
- **Features**: Microphone input processing
- **Language**: Python
- **Size**: Lightweight
- **Best for**: Simple real-time applications

---

## 🧪 **Lightweight & Embedded STT**

### 🔷 [Silero Models](https://github.com/snakers4/silero-models)
- **Type**: Production-ready models
- **Target**: Mobile and edge devices
- **Languages**: Multiple (English, Russian, etc.)
- **Formats**: ONNX, TFLite, TorchScript
- **Best for**: Resource-constrained environments

### 🔷 [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)
- **Type**: Cross-platform real-time ASR
- **Backend**: ONNX
- **Inspiration**: Kaldi and k2 projects
- **Best for**: Cross-platform applications

---

## 📚 **Utility Libraries**

### 🔷 [speech_recognition (Python)](https://github.com/Uberi/speech_recognition)
- **Type**: Unified API wrapper
- **Services**: Google Web Speech, CMU Sphinx, Wit.ai
- **Use case**: Simple applications or prototyping
- **Best for**: Quick prototyping

### 🔷 [annyang (JS)](https://github.com/TalAter/annyang)
- **Type**: Voice command library
- **Target**: Browser applications
- **Size**: Lightweight
- **Best for**: Web-based voice interfaces

---

## 💡 **Selection Guide**

| Use Case | Recommended Model | Why |
|:---|:---|:---|
| **General transcription** | OpenAI Whisper | High accuracy, multilingual |
| **Production deployment** | faster-whisper | Optimized performance |
| **Real-time applications** | Vosk API | Low latency, offline |
| **Research projects** | SpeechBrain | Comprehensive toolkit |
| **Mobile/Edge devices** | Silero Models | Lightweight, efficient |
| **Web applications** | annyang | Browser integration |

---

## 🔗 **Additional Resources**

- **[STT Datasets](./stt-datasets.md)** - Training data for STT models
- **[TTS Models](./tts.md)** - Text-to-speech synthesis
- **[Voice Cloning](./voice-cloning.md)** - Voice synthesis and cloning
- **[Emotion Recognition](./emotion-recognition.md)** - Audio emotion analysis

---

> **💡 Tip**: Choose models based on your deployment target (server, mobile, edge) and language coverage needs.

