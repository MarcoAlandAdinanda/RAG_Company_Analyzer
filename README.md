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
- [Instalasi](#instalasi)
- [Fine-Tuning](#fine-tuning)
- [Deployment](#deployement)
- [Evaluasi](#evaluasi)

## Instalasi
Karena keterbatasan sumber daya GPU, proses fine-tuning model dilakukan menggunakan `Google Colab T4 GPU` untuk menjalankan beberapa notebook dan script, sehingga perlu menginstal packages yang terdapat dalam file `requirements.txt`. Untuk melakukan instalasi, gunakan perintah berikut:

```bash
# installing packages
pip install -r requirements.txt
```

## Fine-Tuning
Retrieval-Augmented Generation (RAG) adalah teknik yang menggabungkan model LLM dengan model embedding. Dalam implementasi ini, dua model yang digunakan adalah:
- **Model LLM**: `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit` (tersedia di HuggingFace)
- **Model Embedding**: `BAAI/bge-m3` (tersedia di HuggingFace)

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

---

Dokumentasi ini bertujuan memberikan gambaran menyeluruh mengenai tim Triwira Data dalam mengembangkan sistem ini, dimulai dari proses instalasi, fine-tuning, deployment, dan evaluasi sistem. Jika ada pertanyaan lebih lanjut atau bantuan yang diperlukan, jangan ragu untuk menghubungi tim Triwira Data melalui channel yang telah tersedia.
