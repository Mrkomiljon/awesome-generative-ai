# Widely-used Transformer Models

> Comprehensive collection of transformer and foundation models for audio, vision, multimodal, and NLP use cases.

---

## Table of Contents
- [Audio Processing](#audio-processing)
- [Computer Vision](#computer-vision)
- [Multimodal](#multimodal)
- [Natural Language Processing](#natural-language-processing)
- [Model Selection Guide](#model-selection-guide)

---

## Audio Processing

### Speech Recognition and Classification
- **[Whisper](https://huggingface.co/openai/whisper-large-v3-turbo)** - Multilingual speech recognition
- **[Moonshine](https://huggingface.co/UsefulSensors/moonshine)** - Automatic speech recognition
- **[Wav2Vec2](https://huggingface.co/superb/wav2vec2-base-superb-ks)** - Keyword spotting

### Audio Generation and Synthesis
- **[Moshi](https://huggingface.co/kyutai/moshiko-pytorch-bf16)** - Speech-to-speech generation
- **[MusicGen](https://huggingface.co/facebook/musicgen-large)** - Text-to-audio generation
- **[Bark](https://huggingface.co/suno/bark)** - Text-to-speech synthesis

---

## Computer Vision

### Image Understanding
- **[SAM](https://huggingface.co/facebook/sam-vit-base)** - Automatic mask generation
- **[DepthPro](https://huggingface.co/apple/DepthPro-hf)** - Depth estimation
- **[DINO v2](https://huggingface.co/facebook/dinov2-base)** - Image classification

### Object Detection and Recognition
- **[SuperGlue Outdoor](https://huggingface.co/magic-leap-community/superglue_outdoor)** - Keypoint detection
- **[SuperGlue](https://huggingface.co/magic-leap-community/superglue)** - Keypoint matching
- **[RT-DETRv2](https://huggingface.co/PekingU/rtdetr_v2_r50vd)** - Object detection

### Pose and Segmentation
- **[VitPose](https://huggingface.co/usyd-community/vitpose-base-simple)** - Pose estimation
- **[OneFormer](https://huggingface.co/shi-labs/oneformer_ade20k_swin_large)** - Universal segmentation
- **[VideoMAE](https://huggingface.co/MCG-NJU/videomae-large)** - Video classification

---

## Multimodal

### Audio-Text Integration
- **[Qwen2-Audio](https://huggingface.co/Qwen/Qwen2-Audio-7B)** - Audio and text to text
- **[LayoutLMv3](https://huggingface.co/microsoft/layoutlmv3-base)** - Document understanding

### Image-Text Processing
- **[Qwen-VL](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)** - Image and text to text
- **[BLIP-2](https://huggingface.co/Salesforce/blip2-opt-2.7b)** - Image captioning
- **[GOT-OCR2](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf)** - OCR document understanding

### Advanced Multimodal
- **[TAPAS](https://huggingface.co/google/tapas-base)** - Table question answering
- **[Emu3](https://huggingface.co/BAAI/Emu3-Gen)** - Unified multimodal understanding
- **[MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o)** - Omni multimodal model from OpenBMB
- **[Llava-OneVision](https://huggingface.co/llava-hf/llava-onevision-qwen2-0.5b-ov-hf)** - Vision to text
- **[Llava](https://huggingface.co/llava-hf/llava-1.5-7b-hf)** - Visual question answering
- **[Kosmos-2](https://huggingface.co/microsoft/kosmos-2-patch14-224)** - Visual referring expression

---

## Natural Language Processing

### Text Understanding
- **[ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base)** - Masked word completion
- **[Gemma](https://huggingface.co/google/gemma-2-2b)** - Named entity recognition
- **[Mixtral](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)** - Question answering

### Text Generation and Processing
- **[BART](https://huggingface.co/facebook/bart-large-cnn)** - Summarization
- **[T5](https://huggingface.co/google-t5/t5-base)** - Translation
- **[Llama](https://huggingface.co/meta-llama/Llama-3.2-1B)** - Text generation
- **[Qwen](https://huggingface.co/Qwen/Qwen2.5-0.5B)** - Text classification

---

## Model Selection Guide

| Task Type | Recommended Models | Typical Use Case |
|:---|:---|:---|
| Speech Recognition | Whisper, Moonshine | Multilingual transcription |
| Image Understanding | SAM, DINO v2 | Visual analysis |
| Multimodal Tasks | Qwen-VL, Llava, MiniCPM-o | Cross-modal reasoning |
| Text Processing | BART, T5, Qwen | Language tasks |
| Audio Generation | MusicGen, Bark | Audio synthesis |

---

## Related Resources

- **[STT Models](./stt-models.md)** - Speech-to-text recognition
- **[TTS Models](./tts.md)** - Text-to-speech synthesis
- **[Text-to-Image](./text-to-image.md)** - Image generation
- **[GenAI APIs](./genai-apis.md)** - API access to models

---

## Best Practices

### Model Selection
- Choose task-specific models first.
- Check resource constraints early.
- Verify licensing for your deployment.
- Prefer models with active maintenance.

### Performance Optimization
- Use quantization for lower cost inference.
- Batch requests for better throughput.
- Cache repeated prompts and embeddings.
- Use GPU acceleration when available.

