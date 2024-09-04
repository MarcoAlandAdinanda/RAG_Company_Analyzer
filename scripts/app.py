import gradio as gr
import ollama
from RAGModule import RAGModule

# Initialize the RAG module
RAG_Triwira = RAGModule()

def chat(message: str, *args):
    """Handles the chat interaction by generating a prompt and streaming the response.

    Args:
        message (str): The user's input message.
        *args: Additional arguments.

    Yields:
        str: The accumulated response text streamed from the model.
    """
    try:
        # Generate the prompt using the RAG module
        prompt = RAG_Triwira.main(message)
        
        # Stream the response from the Ollama API
        stream = ollama.chat(
            model='MarcoAland/llama3.1-rag-indo',
            messages=[{'role': 'user', 'content': prompt}],
            stream=True,
        )

        # Accumulate and yield the response text
        response_text = ''
        for chunk in stream:
            response_text += chunk['message']['content']
            yield response_text

    except Exception as e:
        # Yield the exception message if an error occurs
        yield str(e)

# Define the Gradio interface
iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="Masukan pertanyaan anda", placeholder="Tanyakan saja padaku🌟"),
    outputs=gr.Textbox(label="Respons Mitrakara"),
    title="Hai, namaku Mitrakara. Selamat datang!👋",
    description=(
        '''Berikut adalah beberapa tips untuk bertanya denganku✨✨✨
        1. Gunakan kata 'dokumen:' jika ingin bertanya mengenai dokumen/administrasi perusahaan.
        2. Gunakan kalimat tanya yang baik.
        3. Enjoy the conversation.😊'''
        '''\n\nContoh penggunaan:\n1. Pertanyaan umum: "Beri saya 5 motivasi untuk menjadi pribadi yang lebih baik."
        2. Pertanyaan mengenai administrasi perusahaan: "Dokumen: Siapa nama ketua direksi dan apa saja tanggung jawab beliau."'''
    ),
    examples=[
        ["Beri saya 5 motivasi untuk menjadi pribadi yang lebih baik."],
        ["Dokumen: Siapa nama ketua direksi dan apa saja tanggung jawab beliau."]
    ],
    theme=gr.themes.Soft(),
)

# Launch the Gradio interface
if __name__ == "__main__":
    iface.launch(share=True)  # Generate a public link for any device
