# 🎙️ Speech-to-Text (STT) Datasets

> **Comprehensive collection of high-quality speech datasets for training and evaluating speech recognition models across multiple languages and domains.**

---

## 📋 **Table of Contents**
- [🌍 Multilingual Datasets](#-multilingual-datasets)
- [🇺🇸 English Datasets](#-english-datasets)
- [🌐 Other Languages](#-other-languages)
- [📊 Dataset Statistics](#-dataset-statistics)

---

## 🌍 **Multilingual Datasets**

### 🔷 **Common Voice (Mozilla)**
- **Languages**: 100+ languages
- **Size**: >15,000 hours (validated), >20,000 hours (total)
- **Speakers**: Multi-speaker
- **License**: [CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/)
- **Download**: [voice.mozilla.org](https://voice.mozilla.org/en/datasets)

### 🔷 **VoxForge**
- **Languages**: Multiple languages
- **Size**: Variable by language
- **Speakers**: Community-contributed
- **License**: Various open licenses
- **Download**: [voxforge.org](http://www.voxforge.org/)

---

## 🇺🇸 **English Datasets**

### 🔷 **LibriSpeech**
- **Size**: ~1000 hours
- **Speakers**: 2,484 speakers (1,201 female / 1,283 male)
- **Content**: Audiobooks
- **License**: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Download**: [openslr.org/12](http://www.openslr.org/12/)

### 🔷 **LibriTTS**
- **Size**: 586 hours
- **Speakers**: 2,456 speakers (1,185 female / 1,271 male)
- **Content**: TTS-optimized audiobooks
- **License**: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Download**: [openslr.org/60](http://www.openslr.org/60/)

### 🔷 **VCTK**
- **Size**: 44 hours
- **Speakers**: 109 speakers
- **Content**: Multi-speaker conversations
- **License**: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Download**: [datashare.is.ed.ac.uk](http://datashare.is.ed.ac.uk/download/DS_10283_3443.zip)

### 🔷 **Speech Commands**
- **Size**: 17.8 hours
- **Speakers**: >1,000 speakers
- **Content**: Short command words
- **License**: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Download**: [ai.googleblog.com](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html)

---

## 🌐 **Other Languages**

### 🔷 **German Datasets**
- **Thorsten-21.02-neutral**: ~24 hours, 1 male speaker, [CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/)
- **Thorsten-21.06-emotional**: 2,400 utterances, 8 emotions, [CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/)
- **Telecooperation German**: ~35 hours, ~180 speakers, [CC-BY 2.0](https://creativecommons.org/licenses/by/2.0/)

### 🔷 **Nordic Languages**
- **NST Danish ASR**: 229,992 utterances, 616 speakers, [CC-0](https://creativecommons.org/publicdomain/zero/1.0/)
- **NST Swedish ASR**: 366,000 utterances, 1,000 speakers, [CC-0](https://creativecommons.org/publicdomain/zero/1.0/)
- **NST Norwegian ASR**: 359,760 utterances, 980 speakers, [CC-0](https://creativecommons.org/publicdomain/zero/1.0/)

### 🔷 **African Languages**
- **NCHLT Afrikaans**: 56 hours, 210 speakers, [CC-BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- **NCHLT English**: 56 hours, 210 speakers, [CC-BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- **NCHLT isiZulu**: 56 hours, 210 speakers, [CC-BY 3.0](https://creativecommons.org/licenses/by/3.0/)

### 🔷 **Asian Languages**
- **Zeroth-Korean**: 52.8 hours, 115 speakers, [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Google Javanese**: 296 hours, 1,019 speakers, [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Google Bengali**: 229 hours, 508 speakers, [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## 📊 **Dataset Statistics**

### 🔷 **License Distribution**
| License | Count | Description |
|:---|:---|:---|
| **CC-0** | 15+ | Public domain, no restrictions |
| **CC-BY** | 20+ | Attribution required |
| **CC-BY-SA** | 10+ | Share-alike required |
| **CC-BY-NC** | 5+ | Non-commercial use only |

### 🔷 **Language Coverage**
| Language Family | Languages | Total Hours |
|:---|:---|:---|
| **Indo-European** | 50+ | 10,000+ |
| **Sino-Tibetan** | 10+ | 1,000+ |
| **Afro-Asiatic** | 15+ | 2,000+ |
| **Niger-Congo** | 20+ | 3,000+ |
| **Other** | 30+ | 4,000+ |

---

## 💡 **Dataset Selection Guide**

| Use Case | Recommended Datasets | Why |
|:---|:---|:---|
| **General STT** | LibriSpeech, Common Voice | Large, diverse, well-annotated |
| **Multi-speaker** | VCTK, LibriTTS | Multiple speakers, high quality |
| **Command Recognition** | Speech Commands | Short phrases, commands |
| **Multilingual** | Common Voice | 100+ languages |
| **Research** | NST datasets | Academic quality |

---

## 🔗 **Related Resources**

- **[STT Models](./stt-models.md)** - Speech recognition models
- **[TTS Models](./tts.md)** - Text-to-speech synthesis
- **[Voice Cloning](./voice-cloning.md)** - Voice synthesis
- **[Emotion Recognition](./emotion-recognition.md)** - Audio emotion analysis

---

## 🚀 **Usage Examples**

### Python - Loading LibriSpeech
```python
import torchaudio
from torchaudio.datasets import LIBRISPEECH

# Load dataset
dataset = LIBRISPEECH(
    root="./data",
    url="train-clean-100",
    download=True
)

# Access audio and transcript
waveform, sample_rate, transcript, speaker_id, utterance_id = dataset[0]
```

### Python - Loading Common Voice
```python
from datasets import load_dataset

# Load Common Voice dataset
dataset = load_dataset("mozilla-foundation/common_voice_11_0", "en")

# Access data
audio = dataset["train"][0]["audio"]
text = dataset["train"][0]["sentence"]
```

---

> **💡 Tip**: Start with smaller datasets for prototyping, then scale up to larger datasets for production models.

