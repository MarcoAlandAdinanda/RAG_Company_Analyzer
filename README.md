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
- [Credits](#credits)

## Instalasi

Karena keterbatasan sumber daya GPU, proses pelatihan model dilakukan menggunakan `Google Colab T4 GPU`. Untuk menjalankan ChatBot, Anda hanya perlu menginstal paket-paket yang tercantum dalam file `requirements.txt`. Untuk melakukan instalasi, gunakan perintah berikut:

```bash
# Menginstal paket-paket untuk ChatBot
pip install -r requirements.txt
```

## Fine-Tuning

Retrieval-Augmented Generation (RAG) adalah teknik yang menggabungkan model Language Model (LLM) dengan model embedding. Dalam implementasi ini, dua model yang digunakan adalah:

- **Model LLM**: 
  - `unsloth/llama` (tersedia di HuggingFace)
  - `llama-index` (tersedia di HuggingFace)

- **Model Embedding**:
  - `BAAI/bge-m3` (tersedia di HuggingFace)

## Deployment

Integrasi kedua model tersebut diimplementasikan menggunakan framework Gradio dengan bantuan Ollama untuk deployment model LLM. Proses deployment mencakup:

1. **Integrasi Model**: Menghubungkan model LLM dan model embedding.
2. **Deployment**: Menyebarluaskan model melalui Gradio dan Ollama.

## Evaluasi

Evaluasi dilakukan dengan menguji sistem RAG menggunakan serangkaian pertanyaan untuk menilai kemampuannya dalam memberikan jawaban atau instruksi yang akurat. Hasil evaluasi disajikan dalam tabel berikut:

| Pertanyaan | Jawaban | Skor |
| :--------- | :------ | :---: |
| Seconds    | 301     | 283   |

**Catatan**: Skor merupakan hasil penilaian efektivitas jawaban terhadap pertanyaan yang diajukan.

## Credits

Terima kasih kepada semua kontributor dan pengembang yang telah membantu dalam pembuatan dan pengembangan sistem ini. Khususnya kepada:

- Pengembang model LLM: `unsloth/llama`, `llama-index`
- Pengembang model embedding: `BAAI/bge-m3`
- Tim Gradio dan Ollama untuk dukungan dalam deployment.

---

Dokumentasi ini bertujuan memberikan gambaran menyeluruh tentang proses instalasi, fine-tuning, deployment, dan evaluasi sistem, serta memberikan kredit yang sesuai kepada pihak-pihak yang berkontribusi. Jika ada pertanyaan lebih lanjut atau bantuan yang diperlukan, jangan ragu untuk menghubungi tim pengembang melalui saluran yang tersedia.
