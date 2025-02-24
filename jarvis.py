import os
import subprocess
import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer

# Mengunduh model dan tokenizer yang diperlukan jika belum terinstal
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
base_model = AutoModel.from_pretrained(model_name)

# Menambahkan lapisan klasifikasi di atas model BERT
class ChatbotModel(nn.Module):
    def __init__(self, base_model, num_classes):
        super(ChatbotModel, self).__init__()
        self.base_model = base_model
        self.classifier = nn.Linear(base_model.config.hidden_size, num_classes)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state[:, 0, :]  # Ambil output token [CLS]
        logits = self.classifier(cls_output)
        return logits

# Inisialisasi model
num_classes = 4  # 4 kelas: analisis sistem, menjalankan perintah, membaca file, mengedit file
model = ChatbotModel(base_model, num_classes)

def analyze_system():
    """Contoh analisis sistem."""
    try:
        return subprocess.check_output(['systeminfo'], shell=True).decode()
    except Exception as e:
        return f"Terjadi kesalahan saat menganalisis sistem: {e}"

def execute_command(command):
    """Menjalankan perintah sistem yang aman."""
    allowed_commands = ['dir', 'pwd', 'ls']
    command_parts = command.split()
    
    if command_parts[0] in allowed_commands:
        try:
            return subprocess.check_output(command, shell=True).decode()
        except Exception as e:
            return f"Terjadi kesalahan saat menjalankan perintah: {e}"
    else:
        return "Perintah tidak diizinkan."

def read_file(file_path):
    """Membaca isi file dengan path yang aman."""
    allowed_directories = ['C:\\Users\\Public\\Documents', '/home/public/documents']
    
    for directory in allowed_directories:
        if file_path.startswith(directory):
            try:
                with open(file_path, 'r') as file:
                    return file.read()
            except FileNotFoundError:
                return f"File {file_path} tidak ditemukan."
            except Exception as e:
                return f"Terjadi kesalahan saat membaca file: {e}"
    
    return "Akses ke direktori tidak diizinkan."

def edit_file(file_path, content):
    """Mengedit file dengan konten baru dan path yang aman."""
    allowed_directories = ['C:\\Users\\Public\\Documents', '/home/public/documents']
    
    for directory in allowed_directories:
        if file_path.startswith(directory):
            try:
                with open(file_path, 'w') as file:
                    file.write(content)
                return f"File {file_path} telah diedit."
            except Exception as e:
                return f"Terjadi kesalahan saat mengedit file: {e}"
    
    return "Akses ke direktori tidak diizinkan."

def chatbot_response(user_input):
    """Memberikan respons chatbot berdasarkan input pengguna."""
    inputs = tokenizer(user_input, return_tensors="pt", max_length=512, truncation=True)
    
    with torch.no_grad():
        logits = model(inputs['input_ids'], inputs['attention_mask'])
    
    probs = torch.nn.functional.softmax(logits, dim=-1)
    top_prob, top_class = probs.topk(1)
    
    if top_class.item() == 0:  # Analisis sistem
        return analyze_system()
    
    elif top_class.item() == 1:  # Menjalankan perintah
        command = user_input.split('execute command ', 1)[1]
        return execute_command(command)
    
    elif top_class.item() == 2:  # Membaca file
        file_path = user_input.split('read file ', 1)[1]
        return read_file(file_path)
    
    elif top_class.item() == 3:  # Mengedit file
        parts = user_input.split('edit file ', 1)[1].split(' with ', 1)
        
        if len(parts) < 2 or not all(parts):
            return "Perintah edit salah."
        
        file_path = parts[0]
        content = parts[1]
        
        # Batasi ukuran konten agar tidak terlalu besar
        if len(content) > 10000:
            content = content[:10000] + "\n... (terpotong)"
        
        return edit_file(file_path, content)

# Loop utama chatbot
if __name__ == "__main__":
    print("Selamat datang di Chatbot AI. Ketik 'exit' untuk keluar.")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
