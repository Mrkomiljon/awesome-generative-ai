# 🔊 Text-to-Speech (TTS) Models

> **Curated collection of high-quality open-source TTS models and toolkits for research, production, and multi-language synthesis.**

---

## 📋 **Table of Contents**
- [🐢 High-Fidelity Models](#-high-fidelity-models)
- [⚡ Fast & Efficient Models](#-fast--efficient-models)
- [🔊 Vocoders](#-vocoders)
- [🗣️ Notable TTS Projects](#️-notable-tts-projects)
- [💡 Selection Guide](#-selection-guide)

---

## 🐢 **High-Fidelity Models**

### 🔷 [Tortoise-TTS](https://github.com/neonbjb/tortoise-tts)
- **Type**: High-fidelity voice cloning and generation
- **Features**: Prompt tuning, long-form speech
- **Requirements**: GPU, ≥16GB memory recommended
- **Best for**: High-quality voice synthesis

### 🔷 [VITS (Variational Inference TTS)](https://github.com/jaywalnut310/vits)
- **Type**: End-to-end model combining Tacotron2 + HiFi-GAN
- **Features**: High-quality synthesis, fewer artifacts
- **Performance**: Fast training and inference
- **Best for**: Research and production

### 🔷 [Coqui TTS](https://github.com/coqui-ai/TTS)
- **Type**: Modular, multilingual toolkit
- **Features**: Easy training, fine-tuning, pretrained models
- **Languages**: English, German, French, and more
- **Best for**: Production-ready applications

---

## ⚡ **Fast & Efficient Models**

### 🔷 [Tacotron 2](https://github.com/Rayhane-mamah/Tacotron-2)
- **Type**: Two-stage pipeline (spectrogram + vocoder)
- **Features**: Realistic prosody and intonation
- **Framework**: TensorFlow
- **Best for**: Research and learning

### 🔷 [FastSpeech 2](https://github.com/ming024/FastSpeech2)
- **Type**: Non-autoregressive TTS
- **Features**: High speed and stability
- **Vocoders**: HiFi-GAN, WaveGlow compatible
- **Best for**: Real-time applications

### 🔷 [Glow-TTS](https://github.com/jaywalnut310/glow-tts)
- **Type**: Flow-based TTS architecture
- **Features**: High-performance, parallelizable
- **Best for**: Fast inference scenarios

---

## 🔊 **Vocoders**

> **Vocoders convert spectrograms to audio waveforms**

### 🔷 [HiFi-GAN](https://github.com/jik876/hifi-gan)
- **Type**: Fast, high-quality vocoder
- **Features**: Efficient waveform generation
- **Best for**: Production TTS systems

### 🔷 [WaveGlow](https://github.com/NVIDIA/waveglow)
- **Type**: Real-time waveform generator
- **Features**: NVIDIA-optimized
- **Best for**: GPU-accelerated synthesis

### 🔷 [MelGAN](https://github.com/descriptinc/melgan-neurips)
- **Type**: GAN-based vocoder
- **Features**: Adversarial training
- **Best for**: High-quality audio generation

---

## 🗣️ **Notable TTS Projects**

### 🐟 [Fish-Speech](https://github.com/fishaudio/fish-speech)
- **Type**: Real-time streaming TTS system
- **Features**: High-fidelity, low-latency synthesis
- **Demo**: [https://speech.fish.audio/samples/](https://speech.fish.audio/samples/)
- **Website**: [https://speech.fish.audio/](https://speech.fish.audio/)

### 💞 [Kokoro](https://github.com/hexgrad/kokoro)
- **Type**: Multilingual expressive TTS
- **Features**: Multi-speaker, style control
- **Languages**: Japanese/English
- **PyPI**: [kokoro](https://pypi.org/project/kokoro/)
- **Model**: [Hugging Face](https://huggingface.co/hexgrad/Kokoro)
- **Demo**: [Space](https://huggingface.co/spaces/hexgrad/kokoro-tts)

### 🏔️ [Llasa-TTS](https://llasatts.com/)
- **Type**: Ultra-fast multilingual TTS engine
- **Features**: Streaming, natural prosody
- **Demo**: [Space](https://huggingface.co/spaces/srinivasanbalasubramani/llasa-tts)

### 🔥 [Spark-TTS](https://github.com/sparkaudio/spark-tts)
- **Type**: Modular, real-time neural TTS
- **Features**: Latency-optimized
- **Demo**: [https://sparkaudio.github.io/spark-tts/](https://sparkaudio.github.io/spark-tts/)

### 🗣️ [VITS2](https://github.com/daniilrobnikov/vits2)
- **Type**: Tacotron-style neural TTS
- **Features**: Real-time performance, lightweight
- **Architecture**: Fast and modular
- **Synthesis**: Phoneme-based via `espeak-ng`

---

## 💡 **Selection Guide**

| Use Case | Recommended Model | Why |
|:---|:---|:---|
| **High-quality synthesis** | Tortoise-TTS | Best audio quality |
| **Production deployment** | Coqui TTS | Modular, well-documented |
| **Real-time applications** | FastSpeech 2 | Fast inference |
| **Research projects** | VITS | End-to-end, efficient |
| **Multilingual support** | Kokoro | Japanese/English focus |
| **Streaming applications** | Llasa-TTS | Ultra-fast, streaming |
| **Lightweight deployment** | VITS2 | Small footprint |

---

## 🔗 **Additional Resources**

- **[Voice Cloning](./voice-cloning.md)** - Voice synthesis and cloning techniques
- **[STT Models](./stt-models.md)** - Speech-to-text recognition
- **[Emotion Recognition](./emotion-recognition.md)** - Audio emotion analysis
- **[Talking Head](./talking-head.md)** - Visual speech synthesis

---

## 🚀 **Quick Start Examples**

### Python - Coqui TTS
```python
from TTS.api import TTS
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
tts.tts_to_file("Hello world!", "output.wav")
```

### Python - VITS
```python
import torch
from vits import utils, commons
from vits.models import SynthesizerTrn

# Load model and generate speech
```

---

> **💡 Tip**: Consider your use case (quality vs speed) and target platform when choosing a TTS model.

