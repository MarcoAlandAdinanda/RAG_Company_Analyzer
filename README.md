# AIC_TriwiraData
**Ketua tim:** 
1. Marco Aland Adinanda

**Anggota tim:**
1. Ahmad Wildan Jauharul Fuad
2. Dewi Adelia Priyono

## Overview
Dalam pengembangan talenta (talent growth), langkah awal yang diperlukan, terutama untuk karyawan baru, adalah adaptasi lingkungan. Karyawan baru biasanya menjalani orientasi/onboarding terlebih dahulu setelah diterima oleh suatu perusahaan. Orientasi memiliki dampak yang cukup besar terhadap loyalitas dan produktivitas karyawan. Pada tahap ini, terdapat beberapa tantangan tersendiri, seperti informasi berlebih yang didapat dalam waktu yang cenderung singkat, proses administratif yang rumit, kesenjangan budaya, kurangnya pendampingan yang dikarenakan senior yang sibuk, dll. Penggunaan teknologi Artificial Intelligence (AI) dapat menjadi salah satu solusi untuk menyelesaikan permasalahan-permasalahan tersebut. Teknik yang diimplementasikan dalam pengembangan penelitian ini adalah Retrieval-Augmented Generation (RAG).
 
**Apa itu Retrieval-Augmented Generation (RAG)?**
- RAG adalah teknik yang menggabungkan kemampuanLLM dengan sumber data eksternal. Ini memungkinkan model untuk menghasilkan respons yang lebih akurat dan relevan dengan mengakses informasi dari basis data yang ditentukan

**Apa saja manfaat ChatBot berbasis RAG untuk Perusahaan atau Bisnis?**
- Akses Informasi Cepat dan Akurat: talenta akan mendapatkan informasi yang mereka butuhkan dengan cepat, sehingga akan berdampak kepada efisiensi kerja.
- Meningkatkan Produktivitas: Chatbot juga mampu membantu talent dalam tugas sehari-hari, seperti memberikan motivasi bagi para talent.
- Pembelajaran dan Pengembangan: Dengan diberinya akses langsung ke pengetahuan perusahaan, mendukung pemahaman para stakeholder dalm membuat kebijakan dan prosedur perusahaan/binis.
- Pengambilan Keputusan yang Lebih Baik: Akses cepat ke informasi akurat memungkinkan stakeholders mengkases pengambilan keputusan yang lebih baik dan berdasarkan data asli perusahaan.

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
