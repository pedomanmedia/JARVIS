import os
import sys
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Muat model LLaMA 2.7B
model = AutoModelForSeq2SeqLM.from_pretrained("models/llama-2-7b-chat.Q4_K_M.gguf")
tokenizer = AutoTokenizer.from_pretrained("models/llama-2-7b-chat.Q4_K_M.gguf")

def jarvis(input_text):
    # Tokenisasi input text
    inputs = tokenizer.encode_plus(input_text, return_tensors="pt")

    # Jalankan model LLaMA 2.7B
    outputs = model.generate(inputs["input_ids"], num_beams=4)

    # Dekode output text
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return output_text

def main():
    print("Jarvis siap digunakan!")
    while True:
        user_input = input("Pengguna: ")
        response = jarvis(user_input)
        print("Jarvis:", response)

if __name__ == "__main__":
    main()
