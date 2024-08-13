import gradio as gr
import ollama

from RAGScript import RAGModule

RAG_Trwira = RAGModule()

def response(message, chat_history):
    # if len(chat_history) != 0:
    #     chat_before = chat_history[-1][0]
    #     message = message + " " + chat_before

    prompt = RAG_Trwira.main(message)
    print(prompt) # debugging prompt

    stream = ollama.chat(
                            model='MarcoAland/llama3.1-rag-indo',
                            messages=[{'role': 'user', 'content': prompt}],
                            stream=True,
                        )

    response_text = ''
    for chunk in stream:
        response_text += chunk['message']['content']
        yield response_text

    

# Create the Gradio interface
iface = gr.ChatInterface(
    fn=response,
    title="Ollama Chat Model",
    description="This interface allows you to interact with the Ollama chat model and get responses based on the input context and instruction."
)

# Launch the interface
if __name__ == "__main__":
    RAG_Trwira = RAGModule()
    iface.launch()
