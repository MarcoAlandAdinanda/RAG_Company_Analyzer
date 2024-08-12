# AIC_TriwiraData
**Ketua tim:** 
1. Marco Aland Adinanda

Anggota tim:
1. Ahmad Wildan Jauharul Fuad
2. Dewi Adelia Priyono

## Overview
Perusahaan modern menghadapi tantangan untuk meningkatkan performa kerja karyawan dan efisiensi operasional. Salah satu solusi inovatif adalah penggunaan chatbot berbasis AI, yang menyediakan informasi cepat dan akurat serta membantu dalam penyelesaian tugas sehari-hari. Teknik yang diimplementasikan dalam pengembangan chatbot ini adalah Retrieval-Augmented Generation (RAG).
 
**Apa itu Retrieval-Augmented Generation (RAG)?**
- **Retriever** yang mencari informasi relevan dari basis data atau dokumen berdasarkan query.
- **Generator** yang menyusun respon berbasis bahasa alami dari informasi yang ditemukan, membuat jawaban yang koheren dan mudah dipahami.

**Apa saja manfaat ChatBot berbasis RAG untuk Perusahaan atau Bisnis?**
- Akses Informasi Cepat dan Akurat: Karyawan mendapatkan informasi yang mereka butuhkan dengan cepat, meningkatkan efisiensi kerja.
- Meningkatkan Produktivitas: Chatbot membantu dalam tugas sehari-hari, memungkinkan karyawan fokus pada tugas utama.
- Pembelajaran dan Pengembangan: Chatbot RAG memberikan akses langsung ke pengetahuan perusahaan, mendukung pemahaman kebijakan dan prosedur.
- Pengambilan Keputusan yang Lebih Baik: Akses cepat ke informasi akurat memungkinkan pengambilan keputusan yang lebih baik dan berdasarkan data.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Fine-Tuning](#fine-tuning)
- [Deployment](#deployement)
- [Evaluation](#evaluation)
- [Credits](#creditss)

## Installation
Dikarenakan oleh keterbatasan sumber daya berupa ketersediaan GPU, proses training dilakukan pada `Google Colab T4 GPU`. Sehingga instalasi yang diperlukan hanyalah insatalasi untuk menjalankan ChatBot, yang perlu dilakukan adalah menginstall package yang terdapat pada `requirements.txt` melalui command berikut:

```bash
// installing chatbot packages
pip install -r requirements.txt
```

## Fine-Tuning 
Retrieval-Augmented Generation atau biasa disebut RAG adalah teknik yang menggabungkan model llm dan model embedding, sehingga terdapat 2 model yang digunakan, yaitu: 
- Model LLM: unsloth/llama dan llama-index (HuggingFace)
- Model Embedding: BAAI/bge-m3 (HuggingFace)

## Deployment
Integrasi 2 model tersebut diimplementasikan pada framework gradio dengan bantuan ollama untuk deployment model llm.

## Evaluation
Evaluasi yang dilakukan adalah dengan menguji melalui beberapa pertanyaan, apakah sistem RAG sudah mampu menjawab pertanyaan atau intruksi dengan baik.
| Pertanyaan | Jawaban | Skor |
| :---:   | :---: | :---: |
| Seconds | 301   | 283   |

## Credits
