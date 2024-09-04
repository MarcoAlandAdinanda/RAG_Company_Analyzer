#!/bin/bash

pip install colab-xterm
pip install gradio
pip install ollama
pip install llama-cloud==0.0.13
pip install llama-index==0.10.64
pip install llama-index-embeddings-huggingface==0.2.3
pip install llama-index-cli==0.1.13
pip install llama-index-core==0.10.64
pip install llama-index-legacy==0.9.48
pip install llama-index-readers-file==0.1.33
pip install llama-index-readers-llama-parse==0.1.6
pip install llama-parse==0.4.9

curl -fsSL https://ollama.com/install.sh | sh
nohup ollama serve &

gdown https://drive.google.com/drive/folders/1wXwk4RJ7PSxJBA_d9ZjaPlA6tu-e5jjO -O data --folder