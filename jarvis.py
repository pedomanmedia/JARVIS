import subprocess
import spacy
from langchain.chains import LLMChain
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate

# Load model Llama (gunakan model .gguf dari Hugging Face Hub)
llm = LlamaCpp(
    model_path="models/llama-2-7b-chat.Q4_K_M.gguf",  # Download dari Hugging Face Hub
    temperature=0.5,
    n_ctx=2048,
)

# Load NLP model untuk ekstraksi intent
nlp = spacy.load("en_core_web_sm")

def parse_command(user_input):
    doc = nlp(user_input)
    # Contoh: Deteksi intent "list files"
    if "list" in user_input and "files" in user_input:
        return "ls -l"
    elif "disk usage" in user_input:
        return "df -h"
    # Tambahkan lebih banyak intent sesuai kebutuhan
    else:
        return None

def execute_safe_command(command):
    allowed_commands = ["ls", "df", "date", "echo"]  # Whitelist perintah
    if command.split()[0] not in allowed_commands:
        return "Error: Command not allowed."
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return str(e)

# Contoh interaksi
user_input = input("Tuan, apa perintahmu? ")
command = parse_command(user_input)

if command:
    print(f"Executing: {command}")
    print(execute_safe_command(command))
else:
    # Fallback ke LLM untuk generate command
    prompt = PromptTemplate(
        input_variables=["input"],
        template="Convert this request to a safe Unix command: {input}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    generated_command = chain.run(user_input).strip()
    print(f"Generated command: {generated_command}")
    print(execute_safe_command(generated_command))
