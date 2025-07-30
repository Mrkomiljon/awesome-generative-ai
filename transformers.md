# 📈 Widely-used Transformer Models

> **Comprehensive collection of transformer models and foundation models for various AI tasks including audio, vision, multimodal, and NLP applications.**

---

## 📋 **Table of Contents**
- [🎵 Audio Processing](#-audio-processing)
- [👁️ Computer Vision](#️-computer-vision)
- [🔄 Multimodal](#-multimodal)
- [📝 Natural Language Processing](#-natural-language-processing)

---

## 🎵 **Audio Processing**

### 🔷 **Speech Recognition & Classification**
- **[Whisper](https://huggingface.co/openai/whisper-large-v3-turbo)** - Multilingual speech recognition
- **[Moonshine](https://huggingface.co/UsefulSensors/moonshine)** - Automatic speech recognition
- **[Wav2Vec2](https://huggingface.co/superb/wav2vec2-base-superb-ks)** - Keyword spotting

### 🔷 **Audio Generation & Synthesis**
- **[Moshi](https://huggingface.co/kyutai/moshiko-pytorch-bf16)** - Speech-to-speech generation
- **[MusicGen](https://huggingface.co/facebook/musicgen-large)** - Text-to-audio generation
- **[Bark](https://huggingface.co/suno/bark)** - Text-to-speech synthesis

---

## 👁️ **Computer Vision**

### 🔷 **Image Understanding**
- **[SAM](https://huggingface.co/facebook/sam-vit-base)** - Automatic mask generation
- **[DepthPro](https://huggingface.co/apple/DepthPro-hf)** - Depth estimation
- **[DINO v2](https://huggingface.co/facebook/dinov2-base)** - Image classification

### 🔷 **Object Detection & Recognition**
- **[SuperGlue](https://huggingface.co/magic-leap-community/superglue_outdoor)** - Keypoint detection
- **[SuperGlue](https://huggingface.co/magic-leap-community/superglue)** - Keypoint matching
- **[RT-DETRv2](https://huggingface.co/PekingU/rtdetr_v2_r50vd)** - Object detection

### 🔷 **Pose & Segmentation**
- **[VitPose](https://huggingface.co/usyd-community/vitpose-base-simple)** - Pose estimation
- **[OneFormer](https://huggingface.co/shi-labs/oneformer_ade20k_swin_large)** - Universal segmentation
- **[VideoMAE](https://huggingface.co/MCG-NJU/videomae-large)** - Video classification

---

## 🔄 **Multimodal**

### 🔷 **Audio-Text Integration**
- **[Qwen2-Audio](https://huggingface.co/Qwen/Qwen2-Audio-7B)** - Audio/text to text
- **[LayoutLMv3](https://huggingface.co/microsoft/layoutlmv3-base)** - Document understanding

### 🔷 **Image-Text Processing**
- **[Qwen-VL](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)** - Image/text to text
- **[BLIP-2](https://huggingface.co/Salesforce/blip2-opt-2.7b)** - Image captioning
- **[GOT-OCR2](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf)** - OCR document understanding

### 🔷 **Advanced Multimodal**
- **[TAPAS](https://huggingface.co/google/tapas-base)** - Table question answering
- **[Emu3](https://huggingface.co/BAAI/Emu3-Gen)** - Unified multimodal understanding
- **[Llava-OneVision](https://huggingface.co/llava-hf/llava-onevision-qwen2-0.5b-ov-hf)** - Vision to text
- **[Llava](https://huggingface.co/llava-hf/llava-1.5-7b-hf)** - Visual question answering
- **[Kosmos-2](https://huggingface.co/microsoft/kosmos-2-patch14-224)** - Visual referring expression

---

## 📝 **Natural Language Processing**

### 🔷 **Text Understanding**
- **[ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base)** - Masked word completion
- **[Gemma](https://huggingface.co/google/gemma-2-2b)** - Named entity recognition
- **[Mixtral](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)** - Question answering

### 🔷 **Text Generation & Processing**
- **[BART](https://huggingface.co/facebook/bart-large-cnn)** - Summarization
- **[T5](https://huggingface.co/google-t5/t5-base)** - Translation
- **[Llama](https://huggingface.co/meta-llama/Llama-3.2-1B)** - Text generation
- **[Qwen](https://huggingface.co/Qwen/Qwen2.5-0.5B)** - Text classification

---

## 💡 **Model Selection Guide**

| Task Type | Recommended Models | Use Case |
|:---|:---|:---|
| **Speech Recognition** | Whisper, Moonshine | Multilingual transcription |
| **Image Understanding** | SAM, DINO v2 | Visual analysis |
| **Multimodal Tasks** | Qwen-VL, Llava | Cross-modal understanding |
| **Text Processing** | BART, T5 | Language tasks |
| **Audio Generation** | MusicGen, Bark | Audio synthesis |

---

## 🚀 **Quick Start Examples**

### Python - Hugging Face Transformers
```python
from transformers import pipeline

# Text classification
classifier = pipeline("text-classification", model="Qwen/Qwen2.5-0.5B")
result = classifier("This is a positive sentence!")

# Image captioning
captioner = pipeline("image-to-text", model="Salesforce/blip2-opt-2.7b")
caption = captioner("image.jpg")

# Speech recognition
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3-turbo")
text = transcriber("audio.wav")
```

### Python - Model Loading
```python
from transformers import AutoModel, AutoTokenizer

# Load model and tokenizer
model = AutoModel.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

# Process text
inputs = tokenizer("Your text here", return_tensors="pt")
outputs = model(**inputs)
```

---

## 🔗 **Related Resources**

- **[STT Models](./stt-models.md)** - Speech-to-text recognition
- **[TTS Models](./tts.md)** - Text-to-speech synthesis
- **[Text-to-Image](./text-to-image.md)** - Image generation
- **[GenAI APIs](./genai-apis.md)** - API access to models

---

## 💡 **Best Practices**

### 🔒 **Model Selection**
- **Task-specific** models for better performance
- **Resource constraints** consideration
- **Licensing** and usage terms
- **Community support** and documentation

### 🚀 **Performance Optimization**
- **Model quantization** for efficiency
- **Batch processing** for throughput
- **Caching** for repeated operations
- **GPU acceleration** when available

---

> **💡 Tip**: Start with smaller models for prototyping, then scale up to larger models for production use cases.


