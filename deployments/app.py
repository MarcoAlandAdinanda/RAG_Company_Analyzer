import gradio as gr
import ollama
from RAGModule import RAGModule

# Initialize the RAG module
RAG_Triwira = RAGModule()

def chat(message: str, chat_history: str):
    try:
      prompt = RAG_Triwira.main(message)
      stream = ollama.chat(
                              model='MarcoAland/llama3.1-rag-indo',
                              messages=[{'role': 'user', 'content': prompt}],
                              stream=True,
                          )

      response_text = ''
      for chunk in stream:
          response_text += chunk['message']['content']
          yield response_text
    except Exception as e:
      yield e

# Define the Gradio interface
iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="Masukan pertanyaan anda", placeholder="Tanyakan saja padaku🌟"),
    outputs=gr.Textbox(label="Respons Mitrakara"),
    title="Hai, namaku Mitrakara. Selamat datang!👋",
    description='''Berikut adalah beberapa tips untuk bertanya denganku✨✨✨\n1. Gunakan kata 'dokumen:' jika ingin bertanya mengenai dokumen/administrasi perusahaan.\n2. Gunakan kalimat tanya yang baik.\n3. Enjoy the conversation.😊'''
    + '''\n\nContoh penggunaan:\n1. Pertanyaan umum: "Beri saya 5 motivasi untuk menjadi pribadi yang lebih baik."\n2. Pertanyaan mengenai administrasi perusahaan: "Dokumen: Siapa nama ketua direksi dan apa saja tanggung jawab beliau."''',
    examples=[
        ["Beri saya 5 motivasi untuk menjadi pribadi yang lebih baik."],
        ["Dokumen: Siapa nama ketua direksi dan apa saja tanggung jawab beliau."]
    ],
    theme=gr.themes.Soft(),
)

# Launch the Gradio interface
if __name__ == "__main__":
    iface.launch(share=True) # change "share=False" to make it private