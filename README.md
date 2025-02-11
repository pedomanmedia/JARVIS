# AI Llama Bot 🤖🦙

Bot cerdas berbasis AI yang dapat menjalankan perintah sistem melalui interaksi bahasa alami menggunakan model Llama.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

## 📝 Overview

Bot ini menggabungkan kemampuan:
- **Pemrosesan Bahasa Alami (NLP)** dengan model Llama
- **Eksekusi perintah sistem** yang aman
- **Otomatisasi tugas** melalui chat

## ✨ Fitur Utama

- 🧠 Interaksi natural language dengan model Llama
- ⚡ Eksekusi perintah sistem (Linux/Mac/Windows)
- 🔒 Sistem keamanan berbasis whitelist command
- 🐳 Dukungan Docker untuk isolasi lingkungan
- 📦 Extensible dengan plugin tambahan

## 🛠️ Instalasi

### Prerequisites
- Python 3.8+
- Git
- [Llama Model GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)

### Langkah-langkah
1. Clone repositori:
   ```bash
   git clone https://github.com/username/ai-llama-bot.git
   cd ai-llama-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download model Llama (contoh):
   ```bash
   wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf -O models/llama-2-7b-chat.Q4_K_M.gguf
   ```

## 🚀 Penggunaan
### Konfigurasi Awal
Buat file .env:
```ini
 MODEL_PATH=models/llama-2-7b-chat.Q4_K_M.gguf
 ALLOWED_COMMANDS=ls,df,date,echo
```

### Menjalankan Bot
```bash
python3 jarvis.py
```

Contoh Interaksi:
```
Bot: Cuaca hari ini cerah dengan suhu 25°C.
```

## ⚙️ Konfigurasi
Anda dapat menyesuaikan *'ALLOWED_COMMANDS'* di file *'.env'* untuk menentukan perintah sistem yang diizinkan. Pastikan untuk tidak menambahkan perintah berbahaya.

## 🤝 Kontribusi
Kontribusi sangat diterima! Silakan fork repositori ini dan kirim pull request dengan fitur atau perbaikan yang Anda buat.

## 📜 Lisensi
Proyek ini dilisensikan di bawah MIT License.

## 📚 Referensi
Llama.cpp
LangChain
Hugging Face Hub

## 🛠️ Troubleshooting
Model path tidak ditemukan: Pastikan model Llama telah diunduh dan path di *'.env'* sudah benar.
Kesalahan dependensi: Jalankan pip install -r requirements.txt untuk memastikan semua paket terinstal.
Masalah izin: Pastikan Anda memiliki izin yang tepat untuk menjalankan perintah sistem.
