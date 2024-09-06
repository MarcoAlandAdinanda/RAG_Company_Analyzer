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
        "Berikut adalah beberapa tips untuk bertanya denganku✨✨✨\n1. Gunakan prompt dengan baik dan jelas.\n2. Prompt tidak boleh mengandung ujaran kebencian.\n3. Don't forget to enjoy the conversation.😊 \n\n Referensi format pertanyaan dapat diakses melalui bagian examples."
    ),
    examples=[
        ["Apa visi dan misi perusahaan"],
        ["Saya harus bekerja jam berapa dan pakai pakaian apa"],
        ["Bagaimana jika saya telat/terlambat"],
        ["Sebagai staf penjualan, siapa saja orang yang harus saya kenal"],
        ["Bagaimana gambaran pekerjaan yang harus saya lakukan sebagai staf penjualan"],
        ["Berapa gaji saya sebagai staf penjualan"],
        ["Bagaimana cara kerja lembur dan berapa upahnya"],
        ["Apakah ada jatah cuti, bagaimana caranya"],
        ["Jika saudara saya menikah apakah bisa izin? Bagaimana caranya?"],
        ["Bagaimana sanksi jika saya melanggar peraturan?"],
        ["Beri contoh pelanggaran hingga membuat saya di PHK"],
    ],
    theme=gr.themes.Soft(),
)

# Launch the Gradio interface
if __name__ == "__main__":
    iface.launch(share=True)  # Generate a public link for any device
